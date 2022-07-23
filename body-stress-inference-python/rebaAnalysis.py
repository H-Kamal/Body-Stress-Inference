
import random
import json
from time import sleep

# pose direction is asserted via calculating x distance from left ear to nose.
def CalcUpperArmPosREBA(pose_dir, angle):
	if pose_dir > 0: # facing away from origin.
		angle = -angle # flip angle as facing away has you lifting arms up as negative

	if angle < -20:
		return 2
	elif angle > -20 and angle < 20:
		return 1 # normal range of motion - lowest risk
	elif angle > 20 and angle < 45:
		return 2
	elif angle > 45 and angle < 90:
		return 3
	elif angle > 90:
		return 4

	return -1 # means undefined, if an angle or pose_dir was not provided, then ignore value