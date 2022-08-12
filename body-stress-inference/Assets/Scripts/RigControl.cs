using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;
using System;

public class RigControl : MonoBehaviour
{
    public GameObject humanoid;
    public Vector3 bodyRotation = new Vector3(0, 0, 0);
    RigBone leftUpperArm;
    RigBone leftLowerArm;
    RigBone rightUpperArm;
    RigBone rightLowerArm;
    RigBone rightUpperLeg;
    RigBone rightLowerLeg;
    RigBone leftUpperLeg;
    RigBone leftLowerLeg;
    RigBone trunk;
    RigBone neck;
    void Start()
    {
        leftUpperArm = new RigBone(humanoid, HumanBodyBones.LeftUpperArm);
        leftLowerArm = new RigBone(humanoid, HumanBodyBones.LeftLowerArm);
        rightUpperArm = new RigBone(humanoid, HumanBodyBones.RightUpperArm);
        rightLowerArm = new RigBone(humanoid, HumanBodyBones.RightLowerArm);
        rightUpperLeg = new RigBone(humanoid, HumanBodyBones.RightUpperLeg);
        rightLowerLeg = new RigBone(humanoid, HumanBodyBones.RightLowerLeg);
        leftUpperLeg = new RigBone(humanoid, HumanBodyBones.LeftUpperLeg);
        leftLowerLeg = new RigBone(humanoid, HumanBodyBones.LeftLowerLeg);
        trunk = new RigBone(humanoid, HumanBodyBones.Spine);
        neck = new RigBone(humanoid, HumanBodyBones.Neck);

        humanoid.transform.rotation
          = Quaternion.AngleAxis(bodyRotation.z, new Vector3(0, 0, 1))
          * Quaternion.AngleAxis(bodyRotation.x, new Vector3(1, 0, 0))
          * Quaternion.AngleAxis(90, new Vector3(0, 1, 0));

        // Lowers the arms from the T-Pose to the model's side 
        leftUpperArm.set(-90.0f, 1, 0, 0);
        rightUpperArm.set(-90.0f, 1, 0, 0);

    }
    void Update()
    {
        if (RotationData.rotationDic.Count > 0)
        {
            leftUpperArm.offset((float)(RotationData.rotationDic["leftArmAngle"]), 0, 1, 0);
            // Right arm works opposite to the left arm
            rightUpperArm.offset(-(float)(RotationData.rotationDic["rightArmAngle"]), 0, 1, 0);

            leftLowerArm.offset((float)(RotationData.rotationDic["leftLowerArmAngle"]), 0, 0, 1);
            rightLowerArm.offset((float)(RotationData.rotationDic["rightLowerArmAngle"] + 180), 0, 0, 1);

            trunk.offset((float)(RotationData.rotationDic["trunkAngle"]), 1, 0, 0);

            leftUpperLeg.offset((float)(RotationData.rotationDic["leftUpperLegAngle"] + 180), 1, 0, 0);
            rightUpperLeg.offset((float)(RotationData.rotationDic["rightUpperLegAngle"] - 180), 1, 0, 0);

            leftLowerLeg.offset((float)(RotationData.rotationDic["leftLowerLegAngle"]), 1, 0, 0);
            rightLowerLeg.offset((float)(RotationData.rotationDic["rightLowerLegAngle"]), 1, 0, 0);

            neck.offset((float)(RotationData.rotationDic["neckAngle"]*2), 1, 0, 0);
        }
    }
}
