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
        if(REBA.averageREBAScore != null)
        {
            inputField.text = Math.Ceiling(REBA.averageREBAScore).ToString();
        }
    }
}