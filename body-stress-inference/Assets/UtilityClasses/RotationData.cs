using System.Collections.Generic;
using UnityEngine;


public static class RotationData
{
    static RotationData()
    {
        rotationDic = new Dictionary<string, double>();
    }


    public static IDictionary<string, double> rotationDic { get; set; }

    public static void updateHumanRotationDic(JointData jointData)
    {
        rotationDic["leftArmAngle"] = jointData.leftArmAngle;
        rotationDic["rightArmAngle"] = jointData.rightArmAngle;
    }
}