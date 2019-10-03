import numpy as np

mc_data = np.genfromtxt('Motion_Capture_Data.csv', delimiter=',', skip_header=5, usecols=(range(0,71)))

col_map = {'head_end':2, 'head':8, '*chest':65, 'hip':35, 'upper_arm_l':11, 'lower_arm_l':17, 'hand_l':23, 'upper_leg_l':29, 
           'lower_leg_l':38, 'foot_l':44, 'foot_end_l':50, 'upper_arm_r':14, 'lower_arm_r':20, 'hand_r':26,c'upper_leg_r':32, 
           'lower_leg_r':41, 'foot_r':47, 'foot_end_r':53}

cords = ['x','y','z']


