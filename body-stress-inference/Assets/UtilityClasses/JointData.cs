using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class JointData
{
    public JointData()
    {
        REBAScoreDic = new Dictionary<string, double>();
    }

    public double leftArmAngle { get; set; }
    public double leftLowerArmAngle { get; set; }
    public double rightArmAngle { get; set; }
    public double rightLowerArmAngle { get; set; }
    public double leftUpperLegAngle { get; set; }
    public double rightUpperLegAngle { get; set; }
    public double leftLowerLegAngle { get; set; }
    public double rightLowerLegAngle { get; set; }
    public double trunkAngle { get; set; }
    public double rebaUpperLeftArm { get; set; }
    public double rebaUpperRightArm { get; set; }
    public double rebaLowerLeftArm { get; set; }
    public double rebaLowerRightArm { get; set; }
    public double rebaLegAdj { get; set; }
    public double rebaTrunkAdj { get; set; }
    public double rebaNeck { get; set; }
    public double rebaAverage { get; set; }
    public IDictionary<string, double> REBAScoreDic { get; set; }

    public void updateREBAScoresDic()
    {
        REBAScoreDic["rebaUpperLeftArm"] = rebaUpperLeftArm;
        REBAScoreDic["rebaUpperRightArm"] = rebaUpperLeftArm;
        REBAScoreDic["rebaLowerLeftArm"] = rebaLowerLeftArm;
        REBAScoreDic["rebaLowerRightArm"] = rebaLowerRightArm;
        REBAScoreDic["rebaLegAdj"] = rebaLegAdj;
        REBAScoreDic["rebaTrunkAdj"] = rebaTrunkAdj;
        REBAScoreDic["rebaNeck"] = rebaNeck;
        REBAScoreDic["rebaAverage"] = rebaAverage;
    }
}
