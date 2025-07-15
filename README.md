# 3dof_manipulator
This project aims to devlop understanding of Gazeb/Rviz Simulation of a 

3 Degrees of Freedom Scara Like robot manipulator in ROS Melodic/Noetic.

  Do following in your Ubuntu Terminal:
  
    cd ~/catkin_ws/src
    
    git clone https://github.com/NirajKumarRanjan/3dof_manipulator.git

    cd ~/catkin_ws

    catkin_make

    cd

    roslaunch articulated_robot_simulation robot_gazebo.launch

    roslaunch articulated_robot_simulation robot_control.launch


If everything runs without any error, then run following command:

    rostopic list

    rostopic pub /articulated_robot/joint1_effort_controller/command std_msgs/Float64 "data: 1.0"

It can be repeated for all three joints.

Feel free to contact on my mail ID: nirajkumarranjan@gmail.com, or directly post your queries here.

  
