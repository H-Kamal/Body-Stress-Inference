using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Class converts numerical REBA scores into colors which it stores into a dictionary 
public static class REBA
{

    private static Color lowRiskColor;
    private static Color mediumRiskColor;
    private static Color highRiskColor;

    public static double averageREBAScore;
    private const int LOW = 0;
    private const int MEDIUM = 2;
    private const int HIGH = 4;

    public static IDictionary<string, Color> REBAScoreColors;
    static REBA()
    {
        lowRiskColor = Color.green;
        mediumRiskColor = Color.yellow;
        highRiskColor = Color.red;
        REBAScoreColors = new Dictionary<string, Color>();
    }

    // Goes through every key in the jointData dictionary and associates the keys to their color using the key's values 
    public static void setREBAColors(JointData jointData)
    {
        foreach (KeyValuePair<string, double> kvp in jointData.REBAScoreDic)
        {
            switch (kvp.Value)
            {
                case < MEDIUM:
                    REBAScoreColors[kvp.Key] = lowRiskColor;
                    break;
                case double risk when (risk >= MEDIUM && risk < HIGH):
                    REBAScoreColors[kvp.Key] = mediumRiskColor;
                    break;
                case >= HIGH:
                    REBAScoreColors[kvp.Key] = highRiskColor;
                    break;
            }
        }
      
    }
}
