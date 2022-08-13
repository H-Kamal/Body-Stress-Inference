using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ColorREBARisk : MonoBehaviour
{
    private GameObject upperLeftArm;
    private GameObject lowerLeftArm;
    private GameObject upperRightArm;
    private GameObject lowerRightArm;
    private GameObject leftShin;
    private GameObject rightShin;
    private GameObject leftThigh;
    private GameObject rightThigh;
    private GameObject head;
    private GameObject torso;
    private Renderer upperLeftArmRenderer;
    // Start is called before the first frame update
    void Start()
    {
        upperLeftArm = GameObject.Find("UpperLeftArm");
        lowerLeftArm = GameObject.Find("LowerLeftArm");
        upperRightArm = GameObject.Find("UpperRightArm");
        lowerRightArm = GameObject.Find("LowerRightArm");
        leftShin = GameObject.Find("LeftShin");
        rightShin = GameObject.Find("RightShin");
        leftThigh = GameObject.Find("LeftThigh");
        rightThigh = GameObject.Find("RightThigh");
        head = GameObject.Find("Head");
        torso = GameObject.Find("Torso");
        
        upperLeftArmRenderer = upperLeftArm.GetComponent<Renderer>();
    }

    // Update is called once per frame
    void Update()
    {   
        if(REBA.REBAScoreColors.Count > 0)
        {
            upperLeftArm.GetComponent<Renderer>().material.color  = REBA.REBAScoreColors["rebaUpperLeftArm"];
            lowerLeftArm.GetComponent<Renderer>().material.color  = REBA.REBAScoreColors["rebaLowerLeftArm"];
            upperRightArm.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaUpperRightArm"];
            lowerRightArm.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLowerRightArm"];
            leftThigh.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLegAdj"];
            rightThigh.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLegAdj"];
            leftShin.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLegAdj"];
            rightShin.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLegAdj"];
            torso.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaTrunkAdj"];            
            head.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaNeck"];
        }
    }
}
