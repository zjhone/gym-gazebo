# CMake generated Testfile for 
# Source directory: /home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/xacro
# Build directory: /home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/xacro
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_xacro_nosetests_test "/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/catkin_generated/env_cached.sh" "/home/zjh/anaconda3/envs/lab/bin/python3" "/opt/ros/noetic/share/catkin/cmake/test/run_tests.py" "/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/test_results/xacro/nosetests-test.xml" "--return-code" "\"/usr/bin/cmake\" -E make_directory /home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/test_results/xacro" "/usr/bin/nosetests3 -P --process-timeout=60 --where=/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/xacro/test --with-xunit --xunit-file=/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/test_results/xacro/nosetests-test.xml")
set_tests_properties(_ctest_xacro_nosetests_test PROPERTIES  _BACKTRACE_TRIPLES "/opt/ros/noetic/share/catkin/cmake/test/tests.cmake;160;add_test;/opt/ros/noetic/share/catkin/cmake/test/nosetests.cmake;83;catkin_run_tests_target;/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/xacro/CMakeLists.txt;25;catkin_add_nosetests;/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/xacro/CMakeLists.txt;0;")
subdirs("test")
