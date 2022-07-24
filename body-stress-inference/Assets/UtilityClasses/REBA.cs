using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public static class REBA
{

    private static Color lowRiskColor;
    private static Color mediumRiskColor;
    private static Color highRiskColor;

    private const int LOW = 0;
    private const int MEDIUM = 2;
    private const int HIGH = 4;
    public static Color upperLeftArmColor;
    static REBA()
    {
        lowRiskColor = Color.green;
        mediumRiskColor = Color.yellow;
        highRiskColor = Color.red;

        upperLeftArmColor = Color.white;
    }
    public static void setREBAColors(JointData jointData)
    {
        switch (jointData.rebaUpperLeftArm)
        {
            case < MEDIUM:
                upperLeftArmColor = lowRiskColor;
                break;
            case double risk when (risk >= MEDIUM && risk < HIGH):
                upperLeftArmColor = mediumRiskColor;
                break;
            case >= HIGH:
                upperLeftArmColor = highRiskColor;
                break;
        }
    }
}
