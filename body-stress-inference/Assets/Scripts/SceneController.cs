using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneController : MonoBehaviour
{
    public void LoadResultScene()
    {
        SceneManager.LoadScene("ResultScene");
    }
    public void LoadStartScene()
    {
        SceneManager.LoadScene("StartScene");
    }
}