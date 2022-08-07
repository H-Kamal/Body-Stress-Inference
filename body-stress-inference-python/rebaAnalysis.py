# pose direction is asserted via calculating x distance from left ear to nose.
def CalcUpperArmPosREBA(nose_to_ear_x, elbow_to_hip_x, angle):
	if nose_to_ear_x * elbow_to_hip_x < 0: # facing away from origin.
		angle = -angle # flip angle as facing away has you lifting arms up as negative
	print("reba angle :", angle)
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

	return -1 # means undefined, if an angle or nose_to_ear_dist was not provided, then ignore value

def calcLegAdjustmentsREBA(angle):
	if angle >= 30 and angle < 60:
		return 1
	elif angle >= 60:

	return -1
