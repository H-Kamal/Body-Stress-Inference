using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ColorREBARisk : MonoBehaviour
{
    private GameObject upperLeftArm;
    private Renderer upperLeftArmRenderer;
    // Start is called before the first frame update
    void Start()
    {
        upperLeftArm = GameObject.Find("UpperLeftArm");
        upperLeftArmRenderer = upperLeftArm.GetComponent<Renderer>();
    }

    // Update is called once per frame
    void Update()
    {
        upperLeftArmRenderer.material.color = REBA.upperLeftArmColor;
    }
}
