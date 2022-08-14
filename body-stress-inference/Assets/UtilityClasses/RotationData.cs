using System.Collections.Generic;
using UnityEngine;

// Class stores the rotation data as received from the Python backend
public static class RotationData
{
    static RotationData()
    {
        rotationDic = new Dictionary<string, double>();
    }


    public static IDictionary<string, double> rotationDic { get; set; }

    // Updates a rotation dictionary using JointData
    public static void updateHumanRotationDic(JointData jointData)
    {
        rotationDic["leftArmAngle"] = jointData.leftArmAngle;
        rotationDic["rightArmAngle"] = jointData.rightArmAngle;
        rotationDic["leftLowerArmAngle"] = jointData.leftLowerArmAngle;
        rotationDic["rightLowerArmAngle"] = jointData.rightLowerArmAngle;
        rotationDic["leftUpperLegAngle"] = jointData.leftUpperLegAngle;
        rotationDic["rightUpperLegAngle"] = jointData.rightUpperLegAngle;
        rotationDic["leftLowerLegAngle"] = jointData.leftLowerLegAngle;
        rotationDic["rightLowerLegAngle"] = jointData.rightLowerLegAngle;
        rotationDic["trunkAngle"] = jointData.trunkAngle;
        rotationDic["neckAngle"] = jointData.neckAngle;
    }
}