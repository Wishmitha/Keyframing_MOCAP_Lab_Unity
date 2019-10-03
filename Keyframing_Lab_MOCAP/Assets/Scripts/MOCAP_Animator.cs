using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class MOCAP_Animator : MonoBehaviour
{
    public GameObject rigged_model;
    public TextAsset mocap_data;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void readCSV()
    {
        string[] records = mocap_data.text.Split('\n');
        for (int i = 1; i < records.Length; i++)
        {
            string[] fields = records[i].Split(',');
            
        }
    }
}
