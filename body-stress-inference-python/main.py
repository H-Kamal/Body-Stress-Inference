import pose

def main():
    # MAKE DETECTIONS
    dic = pose.determining_joints()
    
    print(dic)

if __name__ == "__main__":
    main()