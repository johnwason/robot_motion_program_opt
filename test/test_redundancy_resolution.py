import numpy as np
from pathlib import Path
import sys
sys.path.append('../src')
from robot_motion_program_opt.redundancy_resolution.redundancy_resolution import *
from robot_motion_program_opt.toolbox.robots_def import *

def test_m10ia_baseline():
    
    curve_name = 'curve_3'
    robot_name = 'FANUC_m10ia'

    curve_path = 'curve_data/'+curve_name+'/'
    curve = np.loadtxt(curve_path+'Curve_dense.csv',delimiter=',')

    robot=robot_obj(robot_name,'robot_config/'+robot_name+'_robot_default_config.yml',\
                     tool_file_path='tool_config/paintgun.csv',d=50,acc_dict_path='robot_config/'+robot_name+'_acc.pickle')
    
    curve_base,curve_normal_base,curve_js,H = redundancy_resolution_baseline(curve, robot)

    robot_path=curve_path+'/'+robot_name+'/'
    Path(robot_path).mkdir(exist_ok=True)
    save_filepath=curve_path+'/'+robot_name+'/baseline/'
    Path(save_filepath).mkdir(exist_ok=True)

    curve_base = np.hstack((curve_base,curve_normal_base))
    np.savetxt(save_filepath+'Curve_in_base_frame.csv',curve_base,delimiter=',')
    np.savetxt(save_filepath+'Curve_js.csv',curve_js,delimiter=',')
    np.savetxt(save_filepath+'curve_pose.csv',H,delimiter=',')

test_m10ia_baseline()