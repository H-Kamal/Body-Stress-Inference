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
    SAMPLE_SIZE = 2 # Rate at which we send a JSON object of REBA scores and angles
    sampleCount = 0
    avgRebaLeftArm = 0
    avgRebaRightArm = 0
    avgRebaLowerLeftArm = 0
    avgRebaLowerRightArm = 0
    avgRebaLegAdj = 0
    avgRebaTrunk = 0
    avgRebaNeck = 0

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            _, frame = cap.read()
            
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

                # Get coordinates for specific body parts
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

                # Need a landmark of where the person is standing for the trunk angle calculation
                left_hip_bottom = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, 1]
                left_hip_top = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, 0]
                right_hip_top = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, 0]

                right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
           
                # Calculate angles for REBA analysis
                left_arm_angle = cu.calc_cosine_law(left_shoulder, left_elbow, left_hip)
                right_arm_angle = cu.calc_cosine_law(right_shoulder, right_elbow, right_hip)
                left_lower_arm_angle = cu.calc_cosine_law(left_shoulder, left_wrist, left_elbow)
                right_lower_arm_angle = cu.calc_cosine_law(right_elbow, right_shoulder, right_wrist)
                left_adj_angle = cu.calc_cosine_law(left_hip, left_knee, left_ankle)
                left_upper_leg_angle = cu.calc_cosine_law(left_hip, left_knee, left_hip_top)
                right_upper_leg_angle = cu.calc_cosine_law(right_hip, right_knee, right_hip_top)
                left_lower_leg_angle = abs(cu.calc_cosine_law(left_knee, left_hip, left_ankle) - 180)
                right_lower_leg_angle = abs(cu.calc_cosine_law(right_knee, right_hip, right_ankle) - 180)
                trunk_angle = abs(cu.calc_cosine_law(left_hip, nose, left_hip_bottom) - 180) # subtract 180 to get from other side.
                neck_angle = cu.calc_cosine_law(left_shoulder, nose, left_ear)
                
                sampleCount += 1
                if sampleCount >= SAMPLE_SIZE: # take a sample every 2 iterations of the loop
                    rebaLeftArm = rebaAnalysis.CalcUpperArmPosREBA(nose[0] - left_ear[0], left_elbow[0] - left_hip[0], left_arm_angle) # do REBA analysis taken on angle
                    rebaRightArm = rebaAnalysis.CalcUpperArmPosREBA(nose[0] - right_ear[0], right_elbow[0] - right_hip[0], right_arm_angle)
                    rebaLowerLeftArm = rebaAnalysis.calcLowerArmPosREBA(left_lower_arm_angle)
                    rebaLowerRightArm = rebaAnalysis.calcLowerArmPosREBA(right_lower_arm_angle)
                    rebaLegAdj = rebaAnalysis.calcLegAdjustmentsREBA(left_adj_angle)
                    rebaTrunk = rebaAnalysis.calcTrunkREBA(nose[0] - left_ear[0], left_elbow[0] - left_hip[0], trunk_angle)
                    rebaNeck = rebaAnalysis.calcNeckREBA(nose[0] - left_ear[0], nose[0] - left_shoulder[0], neck_angle)

                    # average the REBA score for each body part to get a running count of the total, average REBA score.
                    avgRebaLeftArm = (rebaLeftArm + avgRebaLeftArm) / 2
                    avgRebaRightArm = (rebaRightArm + avgRebaRightArm) / 2
                    avgRebaLowerLeftArm = (rebaLowerLeftArm + avgRebaLowerLeftArm) / 2
                    avgRebaLowerRightArm = (rebaLowerRightArm + avgRebaLowerRightArm) / 2
                    avgRebaLegAdj = (rebaLegAdj + avgRebaLegAdj) / 2
                    avgRebaTrunk = (rebaTrunk + avgRebaTrunk) / 2
                    avgRebaNeck = (rebaNeck + avgRebaNeck) / 2
                    
                    # Average out the REBA scores over the SAMPLE_SIZE before sending over to Unity 
                    rebaTotal = (avgRebaLeftArm + avgRebaRightArm + avgRebaLowerLeftArm + avgRebaLowerRightArm + avgRebaLegAdj + avgRebaTrunk + avgRebaNeck)
                    sampleCount = 0

                    # Data to be sent to Unity
                    body_parts = {
                        "leftArmAngle" : left_arm_angle,
                        "rightArmAngle" : right_arm_angle,
                        "leftLowerArmAngle": left_lower_arm_angle,
                        "rightLowerArmAngle": right_lower_arm_angle,
                        "leftUpperLegAngle": left_upper_leg_angle,
                        "rightUpperLegAngle": right_upper_leg_angle,
                        "leftLowerLegAngle": left_lower_leg_angle,
                        "rightLowerLegAngle": right_lower_leg_angle,
                        "trunkAngle": trunk_angle,
                        "neckAngle": neck_angle,
                        "rebaUpperLeftArm": rebaLeftArm,
                        "rebaUpperRightArm": rebaRightArm,
                        "rebaLowerLeftArm": rebaLowerLeftArm,
                        "rebaLowerRightArm": rebaLowerRightArm,
                        "rebaLegAdj": rebaLegAdj,
                        "rebaTrunk": rebaTrunk,
                        "rebaNeck": rebaNeck, 
                        "rebaTotal": rebaTotal,
                        "avgRebaLeftArm": avgRebaLeftArm,
                        "avgRebaRightArm": avgRebaRightArm,
                        "avgRebaLowerLeftArm": avgRebaLowerLeftArm,
                        "avgRebaLowerRightArm": avgRebaLowerRightArm,
                        "avgRebaLegAdj": avgRebaLegAdj,
                        "avgRebaTrunk": avgRebaTrunk,
                        "avgRebaNeck": avgRebaNeck
                    }      
                    
                    # Connect to waiting Unity server and send it the JSON object with Reba and angle data
                    socket = server.connectSocket(PORT)
                    server.sendJSONDataToUnity(socket, body_parts)
                
            except:
                pass    
                        
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))
            
            cv2.putText(image, "Press 'q' to quit", (0,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.imshow('Mediapipe Feed', image)
            
            # Press the q key on your keyboard to exit out of the image capture
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        
    return body_parts