import numpy as np

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
    
    abDist = np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    acDist = np.sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2)
    bcDist = np.sqrt((b[0]-c[0])**2 + (b[1]-c[1])**2)
    radians = np.arccos((abDist**2 + acDist**2 -bcDist**2) / (2*abDist*acDist)) 
    angle = radians*180.0/np.pi
    return angle