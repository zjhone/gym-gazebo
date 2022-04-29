## *********************************************************
##
## File autogenerated for the create_node package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'update_rate', 'type': 'double', 'default': 30.0, 'level': 0, 'description': 'Polling rate for the irobot create.', 'min': 5.0, 'max': 30.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'drive_mode', 'type': 'str', 'default': 'twist', 'level': 0, 'description': 'The possible drive modes (twist, turtle, drive).', 'min': '', 'max': '', 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'twist', 'type': 'str', 'value': 'twist', 'srcline': 10, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/turtlebot_create/create_node/cfg/TurtleBot.cfg', 'description': 'Takes a geometry_msgs/Twist message and is navigation compatible.', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'turtle', 'type': 'str', 'value': 'turtle', 'srcline': 11, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/turtlebot_create/create_node/cfg/TurtleBot.cfg', 'description': 'Takes a create_node/Turtle message and is turtlesim compatible.', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'drive', 'type': 'str', 'value': 'drive', 'srcline': 12, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/turtlebot_create/create_node/cfg/TurtleBot.cfg', 'description': 'Takes a create_node/Drive message which drives the TurtleBot as described in the iRobot Create manual.', 'ctype': 'std::string', 'cconsttype': 'const char * const'}], 'enum_description': ''}", 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'cmd_vel_timeout', 'type': 'double', 'default': 0.6, 'level': 0, 'description': 'How long to wait before timing out on a velocity command..', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'stop_motors_on_bump', 'type': 'bool', 'default': True, 'level': 0, 'description': 'Stops motors when the bumps sensor is hit.', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'has_gyro', 'type': 'bool', 'default': True, 'level': 0, 'description': 'Enables or disables the gyro.', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'gyro_scale_correction', 'type': 'double', 'default': 1.35, 'level': 0, 'description': 'Scaling factor for correct gyro operation.', 'min': 0.0, 'max': 6.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'gyro_measurement_range', 'type': 'double', 'default': 150.0, 'level': 0, 'description': 'Measurement range supported by gyro.', 'min': 0.0, 'max': 300.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'ADXRS613', 'type': 'double', 'value': 150.0, 'srcline': 24, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/turtlebot_create/create_node/cfg/TurtleBot.cfg', 'description': 'ADXRS613 150deg/s', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ADXRS652', 'type': 'double', 'value': 250.0, 'srcline': 25, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/turtlebot_create/create_node/cfg/TurtleBot.cfg', 'description': 'ADXRS652 250deg/s', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ADXRS642', 'type': 'double', 'value': 300.0, 'srcline': 26, 'srcfile': '/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/turtlebot_create/create_node/cfg/TurtleBot.cfg', 'description': 'ADXRS642 300deg/s', 'ctype': 'double', 'cconsttype': 'const double'}], 'enum_description': 'Gyro Options'}", 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'odom_angular_scale_correction', 'type': 'double', 'default': 1.0, 'level': 0, 'description': 'A correction applied to the computation of the rotation in the odometry.', 'min': 0.0, 'max': 3.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'odom_linear_scale_correction', 'type': 'double', 'default': 1.0, 'level': 0, 'description': 'A correction applied to the computation of the translation in odometry.', 'min': 0.0, 'max': 3.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'min_abs_yaw_vel', 'type': 'double', 'default': 0, 'level': 0, 'description': 'Minimum angular velocity of the TurtleBot.', 'min': 0.0, 'max': 3.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'max_abs_yaw_vel', 'type': 'double', 'default': 0, 'level': 0, 'description': 'Maximum angular velocity of the TurtleBot.', 'min': 0.0, 'max': 3.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

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

TurtleBot_twist = 'twist'
TurtleBot_turtle = 'turtle'
TurtleBot_drive = 'drive'
TurtleBot_ADXRS613 = 150.0
TurtleBot_ADXRS652 = 250.0
TurtleBot_ADXRS642 = 300.0
