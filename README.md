# Octobotics_Coding_Assignment
- steps to run simulation


- run roscore
```bash
roscore
```
- launch the simulation using roslaunch

```bash
roslaunch inverted_pendulum_sim inverted_pendulum_sim.launch
```
- To give sinesoidal input to the force
```bash
rosrun inverted_pendulum_controller sine_force_publisher.py
```
- run the state_publisher.py to give input force to SIP cart model
```bash
rosrun inverted_pendulum_controller state_subscriber.py
```
