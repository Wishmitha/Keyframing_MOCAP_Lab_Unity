using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class MOCAP_Animator : MonoBehaviour
{
    public GameObject game_obj;
    public TextAsset mocap_data;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Animate();
    }

    private void Animate()
    {
        string[] records = mocap_data.text.Split('\n');
        for (int i = 1; i < records.Length; i++)
        {
            string[] fields = records[i].Split(',');
            game_obj.transform.Rotate(float.Parse(fields[0]), float.Parse(fields[1]), float.Parse(fields[2]));
            game_obj.transform.position = new Vector3(float.Parse(fields[0]), float.Parse(fields[1]), float.Parse(fields[2]));
            //Debug.Log(fields[1]);
        }
    }

    private void ReadCSV()
    {

    }
}
