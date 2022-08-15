using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class updateREBAScore : MonoBehaviour
{
    [SerializeField] private TextMeshProUGUI inputField;
    public void Update()
    {
        if(REBA.REBATotal != 0.0d)
        {
            inputField.text = Math.Ceiling(REBA.REBATotal).ToString();
        }
    }
}