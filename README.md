# My Python, AI & IoT Project Space 

Hey there! This repository is a personal sandbox containing hands on projects I built from scratch during my self directed gap year. 

Instead of just following tutorials, I wanted to learn by actually building software and exploring how code interacts with hardware. Inside, you'll find real time computer vision applications, smart hardware automation setups, and command line Python utilities written to practice software fundamentals.

I love taking an idea, figuring out the programming logic behind it and working through the debugging process until everything runs smoothly.

---

## Tech Stack

* **Languages:** Python 3, C/C++ (Arduino)
* **AI & Vision:** OpenCV, MediaPipe, NumPy
* **Hardware & Sensors:** Arduino Uno, Servo Motors, PIR Motion, Sound, Smoke, Soil Moisture Sensors, and I2C LCD Displays
* **Tools:** VS Code, Git, GitHub

---

## Project Breakdown

### 1. Computer Vision & Gesture Control (OpenCV + MediaPipe)
These projects use a standard webcam to capture live video frames, track coordinates for hand landmarks or faces, and translate those movements into instant software commands or hardware actions.
* **Key Projects:** `Pinch Controlled Motor System`, `Hand Gesture LED Controller`, `Virtual Button`, `Face Detection`, and a `Smart Door Lock`.
* **Technical Implementation:** Utilizes a pipeline processing video streams into frame matrices, tracking 2D coordinate hand landmarks via MediaPipe, and calculating spatial transformations to isolate dynamic triggers.
* **Experimental Scripts:** A couple of fun interactive tests including a `Catch the Ball` game, a drawing canvas application, and a WASD motion controller.

### 2. Smart IoT Automation Hub (Arduino Labs)
Interactive hardware setups where I connected different sensors to microcontrollers. This allowed my code to read live data from the physical environment and trigger real-world mechanical responses.
* **Key Projects:** A motion activated alarm system, fire and smoke alerts, automatic soil moisture monitoring, and precise servo motor controls.
*  **Technical Implementation:** Architected circuit blueprints utilizing digital and analog sensor state tracking (Motion, Sound, Smoke, Moisture) integrated via C/C++ scripts to execute automated hardware operations (Servo movement, real time LCD state outputs).
*  **Core Hardware Workspaces:** Explore the `/Arduino` directory for sensor layouts, wiring logic, and firmware implementations.

### 3. Clean Python Utilities
Command line applications built around object oriented concepts to practice building clean, reliable software.
* **Key Projects:** An `ATM System`, `Library Management System`, `Student Record Management`, and an `Expense Tracker`.
* **Technical Focus:** I focused heavily on implementing solid input validation and error handling so the programs stay stable and handle unexpected user inputs without crashing.

---

## Getting Started

To run the vision scripts or Python utilities locally, make sure you have a working webcam connected and run these commands in your terminal:

```bash
# Clone the repository
git clone [https://github.com/Diabohallu/python-iot-portfolio.git](https://github.com/Diabohallu/python-iot-portfolio.git)

# Move into the project folder
cd python-iot-portfolio

# Install the required Python libraries
pip install opencv-python mediapipe numpy pyfirmata
