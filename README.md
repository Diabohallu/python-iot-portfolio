# My Python, AI & IoT Code Space 

Welcome! This repository is a collection of my favorite hands on projects built from scratch during my self directed gap year. It’s a mix of real time computer vision experiments, smart hardware automation setups, and custom Python utilities written to solve practical problems and handle data cleanly.

I love taking an exciting idea, figuring out the programmatic logic behind it, and spending hours debugging until it works flawlessly.

---

## Tech Stack I Use 

* **Languages:** Python 3.x, C/C++ (for Arduino automation)
* **Libraries:** OpenCV, MediaPipe, NumPy, PyFirmata
* **Hardware & Components:** Arduino Uno, PIR motion sensors, Servo motors, and I2C LCD screens

---

## Core Project Modules 

### 1. Computer Vision & Gesture Control (OpenCV + MediaPipe)

* **What it is:** Real-time visual tracking programs that let me control software actions and trigger hardware automation using nothing but hand gestures.
  
* **What it does:** It maps live frames from a webcam, tracks exact hand landmarks, and translates those coordinates into instant commands. I spent a lot of time fine-tuning the coordinates so it doesn't glitch or trigger accidentally when you shift your hand.
  
* **Key Files:** `pinch_controlled_motor_system.py`, `virtual_button.py`, `face_detection.py`

### 2. Smart IoT Automation Hub (Arduino IDE)

* **What it is:** Interactive hardware projects controlled via microcontrollers. I hooked up various sensors to read real-time data and execute physical responses.
  
* **What it does:** It maps live data streams (like motion, sound, or smoke) directly to real-world actions—like automatically rotating a servo motor to open a door or flashing an alert message on an LCD screen when a sensor threshold is crossed.
  
* **Key Folder:** Check out the `/Arduino` directory for the full collection of sensor scripts.

### 3. Clean Python Utilities

* **What it is:** Simple, object-oriented command-line applications built to store, search, and manage data efficiently.
  
* **What it does:** Instead of just writing basic scripts, I focused heavily on building solid input validation and graceful error handling. If a user enters unexpected or chaotic inputs, the programs handle them safely instead of crashing.
  
* **Key Files:** `expense_tracker.py`, `library.py`

---

## Getting Started 

Want to run the vision scripts or utilities locally? Make sure you have a working webcam and run these commands in your terminal:

```bash
# Clone the repository
git clone [https://github.com/Diabohallu/python-iot-portfolio.git](https://github.com/Diabohallu/python-iot-portfolio.git)

# Move into the project directory
cd python-iot-portfolio

# Install the required Python libraries
pip install opencv-python mediapipe numpy
