import gym
import rospy
import roslaunch
import time
import numpy as np

from gym import utils, spaces
from gym_gazebo.envs import gazebo_env
from geometry_msgs.msg import Twist, Point, Pose, Quaternion
from std_srvs.srv import Empty
from sensor_msgs.msg import LaserScan
from gym.utils import seeding
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import GetModelState, SetModelState


class GC2TLEnv(gazebo_env.GazeboEnv):

    def __init__(self):
        # Launch the simulation with the given launchfile name
        gazebo_env.GazeboEnv.__init__(self, "GazeboCircuit2TurtlebotLidar_v1.launch")
        self.vel_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=5)
        self.unpause = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
        self.pause = rospy.ServiceProxy('/gazebo/pause_physics', Empty)
        self.reset_proxy = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)

        self.model_state = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

        self.action_space = spaces.Discrete(3)  #F,B,L,R
        self.reward_range = (-np.inf, np.inf)

        self._seed()

    def discretize_observation(self,data,new_ranges):
        discretized_ranges = []
        min_range = 0.2
        done = False
        mod = len(data.ranges)/new_ranges
        for i, item in enumerate(data.ranges):
            if (i%mod==0):
                if data.ranges[i] == float ('Inf') or np.isinf(data.ranges[i]):
                    discretized_ranges.append(6)
                elif np.isnan(data.ranges[i]):
                    discretized_ranges.append(0)
                else:
                    discretized_ranges.append(int(data.ranges[i]))
            if (min_range > data.ranges[i] > 0):
                done = True
        return discretized_ranges, done

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def getModelStates(self):  # 这个无返回
        rospy.wait_for_service('/gazebo/get_model_state')

        try:
            mobile_base = self.model_state.call("mobile_base", "")
            # print("Turtlebot Pose:", mobile_base.pose.position.x, mobile_base.pose.position.y,
            #       mobile_base.pose.position.z)  # 机器人的位置
            # target = self.model_state.call("Target", "")
            # print("目标点位置:", target.pose.position.x, target.pose.position.y)
        except (rospy.ServiceException) as e:
            print("/gazebo/get_model_state service call failed")

    def getStates(self):   # 有返回
        rospy.wait_for_service('/gazebo/get_model_state')
        try:
            mobile_base = self.model_state.call("mobile_base", "")
            mx = mobile_base.pose.position.x
            my = mobile_base.pose.position.y
            mz = mobile_base.pose.position.z
            # print("机器人位置:", mx, my, mz)  # 机器人的位置
            target = self.model_state.call("Target", "")
            tx = target.pose.position.x
            ty = target.pose.position.y
            # print("目标点位置:", tx, ty)
            return mx, my, tx, ty
        except (rospy.ServiceException) as e:
            print("/gazebo/get_model_state service call failed")
            return 0, 0, 0, 0

    def step(self, action):

        rospy.wait_for_service('/gazebo/unpause_physics')
        try:
            self.unpause()
        except (rospy.ServiceException) as e:
            print("/gazebo/unpause_physics service call failed")

        if action == 0: #FORWARD
            vel_cmd = Twist()
            vel_cmd.linear.x = 0.3
            vel_cmd.angular.z = 0.0
            self.vel_pub.publish(vel_cmd)
        # elif action == 3: #BACKWORD
        #     vel_cmd = Twist()
        #     vel_cmd.linear.x = -0.3
        #     vel_cmd.angular.z = 0.0
        #     self.vel_pub.publish(vel_cmd)
        elif action == 1: #LEFT
            vel_cmd = Twist()
            vel_cmd.linear.x = 0.1
            vel_cmd.angular.z = 0.2
            self.vel_pub.publish(vel_cmd)
        elif action == 2: #RIGHT
            vel_cmd = Twist()
            vel_cmd.linear.x = 0.1
            vel_cmd.angular.z = -0.2
            self.vel_pub.publish(vel_cmd)

        data = None
        while data is None:
            try:
                data = rospy.wait_for_message('/scan', LaserScan, timeout=5)
            except:
                pass

        rospy.wait_for_service('/gazebo/pause_physics')
        try:
            #resp_pause = pause.call()
            self.pause()
        except (rospy.ServiceException) as e:
            print ("/gazebo/pause_physics service call failed")

        state, done = self.discretize_observation(data,5)

        mx, my, tx, ty = self.getStates()

        # if not done:
        #     if action == 0:
        #         reward = 5
        #     else:
        #         reward = 1
        # else:
        #     reward = -200

        if not done:   # 奖励规则
            if (tx-0.5)<=mx<=(tx+0.5) and (ty-0.5)<=my<=(ty+0.5):
                reward = 100
            elif (tx-1)<=mx<=(tx+1) and (ty-1)<=my<=(ty+1):
                reward = 50
            elif (tx-1.5)<=mx<=(tx+1.5) and (ty-1.5)<=my<=(ty+1.5):
                reward = 10
            else:
                if action == 0:
                    reward = 5
                else:
                    reward = 1
        else:
            reward = -200

        # print("当前状态：", state, reward, done)

        return state, reward, done, {}

    def setModelState(self, x=0.0, y=0.0, z=0.0):
        rospy.wait_for_service('/gazebo/set_model_state')
        self.set_model_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        try:
            mds = ModelState()
            mds.model_name = "mobile_base"
            mds.pose.position.x = x
            mds.pose.position.y = y
            mds.pose.position.z = z
            mds.pose.orientation.x = 0.0
            mds.pose.orientation.y = 0.0
            mds.pose.orientation.z = 0.0
            mds.pose.orientation.w = 0.0
            mds.twist.linear.x = 0.0
            mds.twist.linear.y = 0.0
            mds.twist.linear.z = 0.0
            mds.twist.angular.x = 0.0
            mds.twist.angular.y = 0.0
            mds.twist.angular.z = 0.0
            mds.reference_frame = ''
            # print(mds)
            a = self.set_model_state.call(mds)
            self.getModelStates()
            # print("当前状态被被设置为：",mds)
        except (rospy.ServiceException) as e:
            print ("/gazebo/set_model_state service call failed")

    def reset(self):
        # Resets the state of the environment and returns an initial observation.
        rospy.wait_for_service('/gazebo/reset_simulation')
        try:
            #reset_proxy.call()
            self.reset_proxy()
            self.getModelStates()
        except (rospy.ServiceException) as e:
            print ("/gazebo/reset_simulation service call failed")

        # Unpause simulation to make observation
        rospy.wait_for_service('/gazebo/unpause_physics')
        try:
            #resp_pause = pause.call()
            self.unpause()
        except (rospy.ServiceException) as e:
            print ("/gazebo/unpause_physics service call failed")

        #read laser data
        data = None
        while data is None:
            try:
                data = rospy.wait_for_message('/scan', LaserScan, timeout=5)
                # print(data)
            except:
                pass

        rospy.wait_for_service('/gazebo/pause_physics')
        try:
            #resp_pause = pause.call()
            self.pause()
        except (rospy.ServiceException) as e:
            print ("/gazebo/pause_physics service call failed")

        state = self.discretize_observation(data,5)   # 5条激光线

        # print("状态被重置为：", state)

        return state
