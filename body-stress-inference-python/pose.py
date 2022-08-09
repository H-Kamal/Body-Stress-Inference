import cv2
import mediapipe as mp
import server
import rebaAnalysis
import calcUtilities as cu

mp_drawing = mp.solutions.drawing_utils # this gives us all of our drawing utilities
mp_pose = mp.solutions.pose # this is importing our pose estimation models
cap = cv2.VideoCapture(0)

def determining_joints():    
    PORT  = 1755    
    reba_value = 0
    SAMPLE_SIZE = 5
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
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]

                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                
                nose = [landmarks[mp_pose.PoseLandmark.NOSE.value].x,landmarks[mp_pose.PoseLandmark.NOSE.value].y]
                right_ear = [landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].y]
                left_ear = [landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x, landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y]

                left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
           
                # Calculate angle
                left_arm_angle = cu.calc_cosine_law(left_shoulder, left_elbow, left_hip)
                right_arm_angle = cu.calc_cosine_law(right_shoulder, right_elbow, right_hip)
                left_lower_arm_angle = cu.calc_cosine_law(left_shoulder, left_wrist, left_elbow)
                right_lower_arm_angle = cu.calc_cosine_law(right_shoulder, right_wrist, right_elbow)
                leg_adj_angle = cu.calc_cosine_law(left_hip, left_knee, left_ankle)
                trunk_angle = cu.calc_cosine_law(left_hip, nose, left_ankle)
                
                
                # TODO: Add lines 52 to 75 to a function - should return body parts
                if len(angleArr) < SAMPLE_SIZE: # take n samples and calculate average angle based off measurements
                    angleArr.append(left_body_angle)
                else:
                    avgAngle = sum(angleArr) / len(angleArr)
                    rebaLeftArm = rebaAnalysis.CalcUpperArmPosREBA(nose[0] - left_ear[0], left_elbow[0] - left_hip[0], left_arm_angle) # do REBA analysis taken on angle
                    rebaRightArm = rebaAnalysis.CalcUpperArmPosREBA(nose[0] - right_ear[0], right_elbow[0] - right_hip[0], right_arm_angle)
                    rebaLowerLeftArm = rebaAnalysis.calcLowerArmPosREBA(nose[0] - right_ear[0], left_elbow[0] - left_hip[0], left_lower_arm_angle)
                    rebaLowerRightArm = rebaAnalysis.calcLowerArmPosREBA(nose[0] - right_ear[0], right_elbow[0] - right_hip[0], right_lower_arm_angle)
                    rebaLegAdj = rebaAnalysis.calcLegAdjustmentsREBA(leg_adj_angle)
                    rebaTrunkAdj = rebaAnalysis.calcTrunkAdjustmentsREBA(trunk_angle)
                    
                    reba_value = rebaLegAdj
                    angleArr = []
                    
                    body_parts = {
                        "leftShoulder": left_shoulder,
                        "leftElbow" : left_elbow,
                        "leftHip": left_hip,
                        "leftBodyAngle" : left_body_angle,
                        "rightShoulder": right_shoulder,
                        "rightElbow" : right_elbow,
                        "rightHip": right_hip,
                        "rightBodyAngle" : right_body_angle,
                        "rebaUpperLeftArm": rebaLeftArm,
                        "rebaUpperRightArm": rebaRightArm,
                        "rebaLegAdj": rebaLegAdj,
                        "rebaTrunkAdj": rebaTrunkAdj
                    }      
                    
                    socket = server.connectSocket(PORT)
                    server.sendJSONDataToUnity(socket, body_parts)
                
                # Visualize angle
                cv2.putText(image, str(left_body_angle), tuple(np.multiply(left_elbow, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(image, str(right_body_angle), tuple(np.multiply(right_elbow, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            except:
                pass    
            
            #TODO: update the following line so that it works with any angle from without an intermediary variable (not a core issue)
            # Render Reba angle
            cv2.putText(image, 'REBA Score:' + str(reba_value), (0,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                        
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