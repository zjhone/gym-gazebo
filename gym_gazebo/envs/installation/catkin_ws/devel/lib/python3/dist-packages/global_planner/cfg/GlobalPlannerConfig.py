## *********************************************************
##
## File autogenerated for the global_planner package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'lethal_cost', 'type': 'int', 'default': 253, 'level': 0, 'description': 'Lethal Cost', 'min': 1, 'max': 255, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'neutral_cost', 'type': 'int', 'default': 50, 'level': 0, 'description': 'Neutral Cost', 'min': 1, 'max': 255, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'cost_factor', 'type': 'double', 'default': 3.0, 'level': 0, 'description': 'Factor to multiply each cost from costmap by', 'min': 0.01, 'max': 5.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'publish_potential', 'type': 'bool', 'default': True, 'level': 0, 'description': 'Publish Potential Costmap', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'orientation_mode', 'type': 'int', 'default': 1, 'level': 0, 'description': 'How to set the orientation of each point', 'min': 0, 'max': 6, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'None', 'type': 'int', 'value': 0, 'srcline': 14, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/navigation/global_planner/cfg/GlobalPlanner.cfg', 'description': 'No orientations added except goal orientation', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Forward', 'type': 'int', 'value': 1, 'srcline': 15, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/navigation/global_planner/cfg/GlobalPlanner.cfg', 'description': 'Positive x axis points along path, except for the goal orientation', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Interpolate', 'type': 'int', 'value': 2, 'srcline': 17, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/navigation/global_planner/cfg/GlobalPlanner.cfg', 'description': 'Orientations are a linear blend of start and goal pose', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'ForwardThenInterpolate', 'type': 'int', 'value': 3, 'srcline': 18, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/navigation/global_planner/cfg/GlobalPlanner.cfg', 'description': 'Forward orientation until last straightaway, then a linear blend until the goal pose', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Backward', 'type': 'int', 'value': 4, 'srcline': 20, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/navigation/global_planner/cfg/GlobalPlanner.cfg', 'description': 'Negative x axis points along the path, except for the goal orientation', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Leftward', 'type': 'int', 'value': 5, 'srcline': 22, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/navigation/global_planner/cfg/GlobalPlanner.cfg', 'description': 'Positive y axis points along the path, except for the goal orientation', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Rightward', 'type': 'int', 'value': 6, 'srcline': 24, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/navigation/global_planner/cfg/GlobalPlanner.cfg', 'description': 'Negative y axis points along the path, except for the goal orientation', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'How to set the orientation of each point'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'orientation_window_size', 'type': 'int', 'default': 1, 'level': 0, 'description': 'What window to use to determine the orientation based on the position derivative specified by the orientation mode', 'min': 1, 'max': 255, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

GlobalPlanner_None = 0
GlobalPlanner_Forward = 1
GlobalPlanner_Interpolate = 2
GlobalPlanner_ForwardThenInterpolate = 3
GlobalPlanner_Backward = 4
GlobalPlanner_Leftward = 5
GlobalPlanner_Rightward = 6
