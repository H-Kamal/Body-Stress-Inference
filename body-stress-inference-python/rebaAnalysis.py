# pose direction is asserted via calculating x distance from left ear to nose.
def CalcUpperArmPosREBA(nose_to_ear_x, elbow_to_hip_x, angle):
	if nose_to_ear_x * elbow_to_hip_x < 0: # facing away from origin.
		angle = -angle # flip angle as facing away has you lifting arms up as negative
	if angle < -20:
		return 2
	elif angle > -20 and angle < 20:
		return 1 # normal range of motion - lowest risk
	elif angle >= 20 and angle < 45:
		return 2
	elif angle >= 45 and angle < 90:
		return 3
	elif angle >= 90:
		return 4

	return 0 # means undefined, if an angle or nose_to_ear_dist was not provided, then ignore value

# Gives angle made when user is squatting
def calcLegAdjustmentsREBA(angle):
	if angle < 30:
		return 0
	elif angle >= 30 and angle < 60:
		return 1
	elif angle >= 60:
		return 2

	return 0 # means undefined, if an angle or nose_to_ear_dist was not provided, then ignore value

# Gives angle of forearm relative to wrist and shoulder
def calcLowerArmPosREBA(angle):
	angle = abs(angle - 180) # subtract angle so that we get it from the perspective of the hip
	if angle > 0 and angle < 60 :
		return 2
	elif angle >= 60 and angle < 100:
		return 1
	elif angle >= 100:
		return 2

	return 0 # means undefined, if an angle or nose_to_ear_dist was not provided, then ignore value

# Gives angle of how torso bending towards or away from the ground 
def calcTrunkREBA(nose_to_ear_x, elbow_to_hip_x, angle):
    # calculation for backwards movement
	if nose_to_ear_x * elbow_to_hip_x < 0: # facing away from origin.
		angle = -angle # flip angle as facing away has you lifting arms up as negative
	if -20 <= angle <= -10:
		return 2
	elif -10 < angle <= 0:
		return 1
	elif 0 < angle <= 10:
		return 1
	elif 10 < angle <= 20:
		return 2
	elif 20 < angle <= 60:
		return 3
	elif angle < -20:
		return 3
	elif angle > 60:
		return 4
	return 0 # means undefined, if an angle or nose_to_ear_dist was not provided, then ignore value

# Gives angle made by neck moving towards or away from chest
def calcNeckREBA(nose_to_ear_x, nose_to_shoulder_x, angle):
    # calculation for backwards movement
	if (nose_to_ear_x * nose_to_shoulder_x) < 0: # facing away from origin.
		angle = -angle # flip angle as facing away has you lifting arms up as negative
	if 0 < angle <= 20:
		return 1
	elif angle > 20:
		return 2
	elif angle < 0:
		return 2 
	return 0 # means undefined, if an angle or nose_to_ear_dist was not provided, then ignore value
