import cv2
import mediapipe as mp
import numpy as np
import server
import rebaAnalysis
import threading as th


mp_drawing = mp.solutions.drawing_utils # this gives us all of our drawing utilities
mp_pose = mp.solutions.pose # this is importing our pose estimation models
cap = cv2.VideoCapture(0)

def determining_joints():
    # stage = None
    
    PORT  = 1755
    # socketIsOpen = False
    
    # Curl reba_angle variables
    reba_angle = 0
    SAMPLE_SIZE = 10
    angleArr = []
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            
            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            # Make detection
            results = pose.process(image)
            
            # Recolor image to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark
                # Get coordinates
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                
                nose = [landmarks[mp_pose.PoseLandmark.NOSE.value].x,landmarks[mp_pose.PoseLandmark.NOSE.value].y]
                right_ear = [landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].y]
                left_ear = [landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x, landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y]
                
                
                # print("Nose - right ear: ", nose[0] - right_ear[0], 
                #       "\nnose - left ear: ", nose[0] - left_ear[0], 
                #       "\nright ear - left ear: ", left_ear[0] - right_ear[0],
                #       "\n")

                                
                # Calculate angle
                # left_body_angle = calculate_angle(left_hip, left_shoulder, left_elbow)                
                # right_body_angle = calculate_angle(right_hip, right_shoulder, right_elbow)
                left_body_angle = calc_cosine_law(left_hip, left_shoulder, left_elbow)
                right_body_angle = calc_cosine_law(left_hip, left_shoulder, left_elbow)
                
                if len(angleArr) < SAMPLE_SIZE: # take n samples and calculate average angle based off measurements
                    angleArr.append(left_body_angle)
                else:
                    avgAngle = sum(angleArr) / len(angleArr)
                    rebaLeftArm = rebaAnalysis.CalcUpperArmPosREBA(nose[0] - left_ear[0], left_body_angle) # do REBA analysis taken on angle
                    reba_angle = rebaLeftArm # this needs to be removed
                    print(rebaLeftArm)
                    angleArr = []
                    
                    body_parts = {
                        "Left Shoulder": left_shoulder,
                        "Left Elbow" : left_elbow,
                        "Left Hip": left_hip,
                        "Left Body Angle" : left_body_angle,
                        "Right Shoulder": right_shoulder,
                        "Right Elbow" : right_elbow,
                        "Right Hip": right_hip,
                        "Right Body Angle" : right_body_angle,
                        "Reba Upper Left Arm": rebaLeftArm
                    }      
                    
                    socket = server.connectSocket(PORT)
                    server.sendJSONDataToUnity(socket, body_parts)
                
                # Visualize angle
                cv2.putText(image, str(left_body_angle), tuple(np.multiply(left_elbow, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(image, str(right_body_angle), tuple(np.multiply(right_elbow, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                
                # Curl reba_angle logic
                # if angle > 160:
                #     stage = "down"
                # if angle < 30 and stage =='down':
                #     stage="up"
                #     reba_angle +=1
            except:
                pass    
            
            # Render Reba angle
            cv2.putText(image, 'REBA Angle:' + str(reba_angle), (0,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                        
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))
            
            cv2.imshow('Mediapipe Feed', image)
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        
    return body_parts
        
        
def calculate_angle(a, b, c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = radians*180.0/np.pi
    
    if angle > 180.0:
        angle = 360-angle
    
    return angle 

def calc_cosine_law(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    aDist = np.sqrt((c[0]-b[0])**2 + (c[1]-b[1])**2)
    bDist = np.sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2)
    cDist = np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    radians = np.arccos((aDist**2 + bDist**2 -cDist**2) / (2*aDist*bDist)) 
    angle = radians*180.0/np.pi
    return angle