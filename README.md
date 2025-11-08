# ROS Part A — Robot Programming and Simulation Lab

This repository contains **ROS 2 Part A programs** for the *Robot Programming and Simulation Lab* course.  
All programs are implemented in **Python (rclpy)** and tested on **ROS 2 Humble Hawksbill**.

---

## Project Structure

```
ROS_PARTA/
├── src/
│   └── exam_pkg/
│       ├── exam_pkg/
│       │   ├── __init__.py
│       │   ├── exam_publisher.py
│       │   ├── exam_subscriber.py
│       │   ├── first.py
│       │   ├── hi_node.py
│       │   └── multi_pub.py
├── package.xml
├── setup.cfg
├── setup.py
└── README.md
```

---

## Questions

| Questions | Description | Node File |
|------|--------------|-----------|
| **1** | Create and activate a new ROS 2 workspace `exam_ws`, add Python package `exam_pkg`, and build the workspace. Implement an **object-oriented (class-based)** publisher node that publishes to `/oop_status`. | `first.py` |
| **2** | Create a ROS 2 node using OOP that prints `"Hi I am ROS2"` continuously at **0.5 Hz** until manually killed. | `hi_node.py` |
| **3** | Implement a publisher node that publishes `"Lab Exam in Progress"` to topic `/exam_status`. | `exam_publisher.py` |
| **4** | Implement a subscriber node that listens to `/exam_status` and prints received messages. Run both publisher and subscriber together. | `exam_publisher.py`, `exam_subscriber.py` |
| **5** | Create a single node that publishes to **two topics**: `/exam_text` (string) and `/exam_number` (integer). Demonstrate both using `ros2 topic echo`. | `multi_pub.py` |

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Awshae/ROS_PROGRAMS.git
cd ROS_PARTA
```

### 2. Build the workspace
```bash
colcon build
```

### 3. Source the setup script
```bash
source install/setup.bash
```

---

## Running the Nodes

Use the following format to run each node:
```bash
ros2 run exam_pkg <node_name>
```

### Example Commands
```bash
# Question 1
# create a pkg using 'ros2 pkg create exam_pkg --build-type ament_python --dependencies rclpy 
ros2 run exam_pkg first
# Open another terminator window
. install/setup.bash
ros2 topic list 
ros2 topic echo /oops_status

# Question 2
# Run "Hi I am ROS2" Node 
ros2 run exam_pkg hi_node

# Question 3
# Run Exam Publisher 
ros2 run exam_pkg exam_publisher
ros2 topic list 
ros2 topic echo /exam_publisher

# Question 4
# Run Exam Subscriber 
ros2 run exam_pkg exam_publisher
# window 1
ros2 topic echo /exam_publisher
# window 2
ros2 run exam_pkg exam_subscriber

# Question 5
# Run Multi Publisher 
ros2 run exam_pkg multi_pub
# window 1
ros2 topic echo /exam_text
# window 2
ros2 run exam_pkg exam_number
```

## Notes

- Ensure the workspace is sourced every time you open a new terminal:
  ```bash
  source install/setup.bash
  ```
- Tested on **Ubuntu 22.04 LTS** with **ROS 2 Humble Hawksbill**.

---
