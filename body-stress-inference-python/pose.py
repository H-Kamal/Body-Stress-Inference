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
    PORT  = 1755
    socketIsOpen = False
    # Curl counter variables
    counter = 0 
    stage = None
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
                left_body_angle = calculate_angle(left_hip, left_shoulder, left_elbow)
                right_body_angle = calculate_angle(right_hip, right_shoulder, right_elbow)
                
                if len(angleArr) < SAMPLE_SIZE: # take n samples and calculate average angle based off measurements
                    angleArr.append(left_body_angle)
                else:
                    avgAngle = sum(angleArr) / len(angleArr)
                    print(avgAngle)
                    rebaLeftArm = rebaAnalysis.CalcUpperArmPosREBA(nose[0] - left_ear[0], avgAngle) # do REBA analysis taken on angle
                    counter = rebaLeftArm
                    print("reba left arm: ", rebaLeftArm)
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
                
                # Curl counter logic
                # if angle > 160:
                #     stage = "down"
                # if angle < 30 and stage =='down':
                #     stage="up"
                #     counter +=1
            except:
                pass    
            
            # Render curl counter
            # Setup status box
            cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
            
            # # Rep data
            # cv2.putText(image, 'REPS', (15,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
            
            # # Stage data
            # cv2.putText(image, 'STAGE', (65,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            # cv2.putText(image, stage, (60,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
            
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