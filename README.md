# threefinger_publisher
A ROS2 based message publisher node for three finger tool

To build only the my_package package next time, you can run:

```console
colcon build --packages-select threefinger_publisher
```

run the keyboard based publisher node:

```
ros2 run threefinger_publisher keyboard_publisher
```
or for test 
```
ros2 run threefinger_publisher timed_publisher
```

To see the data being published on a topic, use:

```
ros2 topic echo /joint_angles
```

you can monitor the values in rqt plot by looking at:

```
/joint_angles/data[0]
/joint_angles/data[1]
/joint_angles/data[2]

```

