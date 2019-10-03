using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class MOCAP_Animator : MonoBehaviour
{
    public GameObject game_obj;
    public TextAsset mocap_data;

    private string[] frames;
    private int frame_num = 1;

    // Start is called before the first frame update
    void Start()
    {
        frames = mocap_data.text.Split('\n');
    }

    // Update is called once per frame
    void Update()
    {
        Animate();
        frame_num++;
    }

    private void Animate()
    {
        string[] coordinates = frames[frame_num].Split(',');
        Vector3 pos = new Vector3(float.Parse(coordinates[0]), float.Parse(coordinates[1]), float.Parse(coordinates[2]));
        game_obj.transform.position = pos;
        Debug.Log(float.Parse(coordinates[0]));
    }
}
