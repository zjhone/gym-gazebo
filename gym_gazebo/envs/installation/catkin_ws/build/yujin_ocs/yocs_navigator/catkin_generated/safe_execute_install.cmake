execute_process(COMMAND "/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/yujin_ocs/yocs_navigator/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/zjh/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/build/yujin_ocs/yocs_navigator/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
