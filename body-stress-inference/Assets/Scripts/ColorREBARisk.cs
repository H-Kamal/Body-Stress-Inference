using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

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
    private GameObject leftWrist;
    private GameObject rightWrist;
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
        leftWrist = GameObject.Find("LeftWrist");
        rightWrist = GameObject.Find("RightWrist");
        
        upperLeftArmRenderer = upperLeftArm.GetComponent<Renderer>();
    }

    // Update is called once per frame
    void Update()
    {   
        if (REBA.REBAScoreColors.Count > 0)
        {
            if (SceneManager.GetActiveScene() == SceneManager.GetSceneByName("StartScene"))
            {
                upperLeftArm.GetComponent<Renderer>().material.color  = REBA.REBAScoreColors["rebaUpperLeftArm"];
                lowerLeftArm.GetComponent<Renderer>().material.color  = REBA.REBAScoreColors["rebaLowerLeftArm"];
                upperRightArm.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaUpperRightArm"];
                lowerRightArm.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLowerRightArm"];
                leftThigh.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLegAdj"];
                rightThigh.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLegAdj"];
                leftShin.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLegAdj"];
                rightShin.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLegAdj"];
                torso.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaTrunk"];            
                head.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaNeck"];
                leftWrist.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLowerLeftArm"];
                rightWrist.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["rebaLowerRightArm"];
            }
            else if (SceneManager.GetActiveScene() == SceneManager.GetSceneByName("ResultScene"))
            {
                upperLeftArm.GetComponent<Renderer>().material.color  = REBA.REBAScoreColors["avgRebaLeftArm"];
                lowerLeftArm.GetComponent<Renderer>().material.color  = REBA.REBAScoreColors["avgRebaLowerLeftArm"];
                upperRightArm.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["avgRebaRightArm"];
                lowerRightArm.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["avgRebaLowerRightArm"];
                leftThigh.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["avgRebaLegAdj"];
                rightThigh.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["avgRebaLegAdj"];
                leftShin.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["avgRebaLegAdj"];
                rightShin.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["avgRebaLegAdj"];
                torso.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["avgRebaTrunk"];            
                head.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["avgRebaNeck"];
                leftWrist.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["avgRebaLowerLeftArm"];
                rightWrist.GetComponent<Renderer>().material.color = REBA.REBAScoreColors["avgRebaLowerRightArm"];
            }
        }
    }
}
