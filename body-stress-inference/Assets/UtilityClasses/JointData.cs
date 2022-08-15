using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Class recieves the deserialized JSON object sent from the Python backend and stores it into a dictionary
public class JointData
{
    public JointData()
    {
        REBAScoreDic = new Dictionary<string, double>();
    }

    // Angles of body parts at every capture
    public double leftArmAngle { get; set; }
    public double leftLowerArmAngle { get; set; }
    public double rightArmAngle { get; set; }
    public double rightLowerArmAngle { get; set; }
    public double leftUpperLegAngle { get; set; }
    public double rightUpperLegAngle { get; set; }
    public double leftLowerLegAngle { get; set; }
    public double rightLowerLegAngle { get; set; }
    public double trunkAngle { get; set; }
    public double neckAngle { get; set; }
    
    // Reba scores at each capture
    public double rebaUpperLeftArm { get; set; }
    public double rebaUpperRightArm { get; set; }
    public double rebaLowerLeftArm { get; set; }
    public double rebaLowerRightArm { get; set; }
    public double rebaLegAdj { get; set; }
    public double rebaTrunk { get; set; }
    public double rebaNeck { get; set; }
    public double rebaTotal { get; set; }

    // Averages of the bodyparts over the entire length of sensing
    public double avgRebaLeftArm { get; set; }
    public double avgRebaRightArm { get; set; }
    public double avgRebaLowerLeftArm { get; set; }
    public double avgRebaLowerRightArm { get; set; }
    public double avgRebaLegAdj { get; set; }
    public double avgRebaTrunk { get; set; }
    public double avgRebaNeck { get; set; }

    public IDictionary<string, double> REBAScoreDic { get; set; }

    // Updates a dictionary which associates body part strings to their REBA scores as received from Python
    public void updateREBAScoresDic()
    {
        REBAScoreDic["rebaUpperLeftArm"] = rebaUpperLeftArm;
        REBAScoreDic["rebaUpperRightArm"] = rebaUpperRightArm;
        REBAScoreDic["rebaLowerLeftArm"] = rebaLowerLeftArm;
        REBAScoreDic["rebaLowerRightArm"] = rebaLowerRightArm;
        REBAScoreDic["rebaLegAdj"] = rebaLegAdj;
        REBAScoreDic["rebaTrunk"] = rebaTrunk;
        REBAScoreDic["rebaNeck"] = rebaNeck;
        REBAScoreDic["rebaTotal"] = rebaTotal;

        REBAScoreDic["avgRebaLeftArm"] = avgRebaLeftArm;
        REBAScoreDic["avgRebaRightArm"] = avgRebaRightArm;
        REBAScoreDic["avgRebaLowerLeftArm"] = avgRebaLowerLeftArm;
        REBAScoreDic["avgRebaLowerRightArm"] = avgRebaLowerRightArm;
        REBAScoreDic["avgRebaLegAdj"] = avgRebaLegAdj;
        REBAScoreDic["avgRebaTrunk"] = avgRebaTrunk;
        REBAScoreDic["avgRebaNeck"] = avgRebaNeck;

        Debug.Log("'avgRebaLeftArm': " + REBAScoreDic["avgRebaLeftArm"]);
        Debug.Log("'avgRebaRightArm': " + REBAScoreDic["avgRebaRightArm"]);
        Debug.Log("'avgRebaLowerLeftArm': " + REBAScoreDic["avgRebaLowerLeftArm"]);
        Debug.Log("'avgRebaLowerRightArm': " + REBAScoreDic["avgRebaLowerRightArm"]);
        Debug.Log("'avgRebaLegAdj': " + REBAScoreDic["avgRebaLegAdj"]);
        Debug.Log("'avgRebaTrunk': " + REBAScoreDic["avgRebaTrunk"]);
        Debug.Log("'avgRebaNeck': " + REBAScoreDic["avgRebaNeck"]);


    }
}
