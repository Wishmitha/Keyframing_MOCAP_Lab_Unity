import numpy as np
import pandas as pd
import json
import sys,os

dirname = os.path.dirname(__file__)

mc_data = np.genfromtxt('Motion_Capture_Data.csv', delimiter=',', skip_header=5, usecols=(range(0,71)))
mc_data_df = pd.read_csv('Motion_Capture_Data.csv', sep=',',header=[0,1], skiprows=3)
mc_data_df = mc_data_df.drop([1])

game_objects = ['Head_End','Head','Chest','Hip','Upper_Arm_L','Lower_Arm_L','Hand_L','Upper_Leg_L','Lower_Leg_L',
                'Foot_L','Foot_End_L','Upper_Arm_R','Lower_Arm_R','Hand_R','Upper_Leg_R','Lower_Leg_R','Foot_R',
                'Foot_End_R']
markers = ['Top.Head','Rear.Head','R.Scapula','Sacral','L.Shoulder','L.Elbow','L.Wrist','L.ASIS','L.Knee','L.Ankle','L.Toe',
           'R.Shoulder','R.Elbow','R.Wrist','R.ASIS','R.Knee','R.Ankle','R.Toe']

columns = ['Time'] + markers

mc_data_df = mc_data_df[columns]

mc_data_df.to_csv('mc_data_filtered.csv', index=False)

object_marker_map = dict(zip(game_objects, markers))
marker_object_map = dict(zip(markers, game_objects))

for marker in markers:
    df = mc_data_df[marker]
    df.to_csv(dirname + '/Marker Positions/'+ marker_object_map[marker] + '.csv', index=False)


with open('object_marker_map.json', 'w') as fp:
    json.dump(object_marker_map, fp)


    
    
