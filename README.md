# My Python & IoT Project Sandbox 

Welcome! This repository is a collection of my favorite hands on projects, built during my self directed gap year. It’s a mix of computer vision experiments, automated hardware setups, and a few handy Python utilities I wrote to solve practical problems. 

I love taking an idea, figuring out how to write the logic for it, and most importantly, spending hours debugging it until it actually works flawlessly. 

## Tech I Use

*   **Languages:** Python 3.x, C/C++ (for Arduino automation)
*   **Libraries:** OpenCV, MediaPipe, Numpy, PyFirmata
*   **Hardware:** Arduino Uno, PIR motion sensors, Servo motors, and LCD screens

---

## Featured Projects 

### 1. Computer Vision & Gesture Control System
*   **What it is:** A real time gesture recognition program that lets me control software actions and trigger hardware automation using nothing but hand gestures.
*   **The cool part:** It tracks exact hand landmarks using MediaPipe and translates coordinates into application commands. I spent a ton of time fine tuning the responsiveness so it doesn’t accidentally trigger when you just shift your hand.
*   **Core Files:** `pinch_controlled_motor_system.py`, `virtual_button.py`

### 2. IoT Automation Hub
*   **What it is:** Hardware automation projects controlled via Arduino. I hooked up various sensors (like motion, sound and smoke detectors) to execute live responses.
*   **What it does:** It maps live data streams directly to physical hardware actions, like rotating a servo motor or flashing an alert on an LCD screen when a threshold is breached. 
*   **Core Folders:** Look inside the `/Arduino` directory for specific sensor setups.

### 3. Python Data Management Utilities
*   **What it is:** A set of clean, object-oriented command-line applications to store, search, and update data efficiently.
*   **What it does:** Instead of just basic scripts, I focused heavily on building solid input validation and handling errors gracefully so the programs don't crash when you give them unexpected inputs.
*   **Core Files:** `expense_tracker.py`, `library.py`

---

## Getting Started 

If you want to play around with the vision scripts, you'll need a webcam and a few dependencies:

1. Clone the repository:
   ```bash
   [https://github.com/Diabohallu/python-iot-portfolio.git](https://github.com/Diabohallu/python-iot-portfolio.git)
