# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/usr/local/include".split(';') if "${prefix}/include;/usr/local/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;actionlib;tf;yocs_math_toolkit;move_base_msgs;nav_msgs;yocs_msgs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lyocs_basic_move_controller;-lyocs_semantic_navigator;/usr/local/lib/libboost_system.so.1.71.0".split(';') if "-lyocs_basic_move_controller;-lyocs_semantic_navigator;/usr/local/lib/libboost_system.so.1.71.0" != "" else []
PROJECT_NAME = "yocs_navigator"
PROJECT_SPACE_DIR = "/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/install"
PROJECT_VERSION = "0.8.2"
