# 🎯 ESP32-CAM Ball Detector (OpenCV + Python)

An IoT + Computer Vision project that detects and tracks a colored ball in real-time using an ESP32-CAM and Python OpenCV.

---

## 📌 Project Overview

This project combines:
- 📷 ESP32-CAM (image capture + web server)
- 🌐 Wi-Fi (local network streaming)
- 🧠 Python + OpenCV (image processing & detection)

The ESP32-CAM streams JPEG images over HTTP, and a Python script processes those images to detect and track a colored ball.

---

## ⚙️ Features

- 📡 Live image streaming over Wi-Fi  
- 🎯 Real-time ball detection using OpenCV  
- 🎨 Color-based object tracking (HSV filtering)  
- 🔵 Detects position and size of the ball  
- 🖥️ Live visualization with annotations  
- 🔁 Works entirely on a local network (no internet required)  

---

## 🧠 System Architecture

### 1. Hardware Layer
- ESP32-CAM captures images (800×600 resolution)
- Hosts HTTP server
- Serves images at endpoint: `/cam-hi.jpg`

### 2. Network Layer
- ESP32-CAM connects to Wi-Fi
- Host PC accesses image via local IP  
  Example: `http://192.168.x.x/cam-hi.jpg`

### 3. Application Layer
- Python script fetches images
- OpenCV processes frames
- Detects and tracks the ball

---

## 🧰 Components Required

| Component | Quantity |
|----------|---------|
| ESP32-CAM Module | 1 |
| FTDI USB-to-Serial Converter | 1 |
| Jumper Wires | Few |
| Micro USB Cable | 1 |

---

## 🔌 Circuit Connections

| ESP32-CAM | FTDI |
|----------|------|
| VCC | 5V |
| GND | GND |
| U0R | TX |
| U0T | RX |
| IO0 | GND (only during programming) |

⚠️ After uploading code:
- Disconnect IO0 from GND
- Press RESET

---

## 🌐 How It Works

1. ESP32-CAM connects to Wi-Fi
2. Hosts an HTTP server
3. Python script requests images continuously
4. Images are decoded using NumPy + OpenCV
5. Image is converted to HSV color space
6. Mask is applied to isolate ball color
7. Contours are detected
8. Largest contour is tracked as the ball
9. Position and radius are displayed

---

## 🧪 Detection Pipeline

- Convert image → HSV  
- Apply color threshold (red in this case)  
- Clean mask (erosion + dilation)  
- Find contours  
- Select largest contour  
- Draw circle and coordinates  

---

## 🖥️ Python Environment Setup

### 1. Install Python
- Version 3.7 or higher

### 2. Create Virtual Environment
```bash
python -m venv balltrack-env
Activate:
# Windows
balltrack-env\Scripts\activate

# macOS/Linux
source balltrack-env/bin/activate

```
### 3. Install Dependencies

```bash
pip install opencv-python
pip install numpy
pip install requests
```

---

## 📂 Project Structure

```
/project-folder
│
├── ESP32-CAM firmware (Arduino code)
└── Python ball tracking script
```


## 📂 Test
```
Upload the ESP32_Cam_basic.ino code to the ESP32 cam and run the python code in your computer while the ESP32 is connected to it.
Test the code with a ball visible in the camera. 
```
