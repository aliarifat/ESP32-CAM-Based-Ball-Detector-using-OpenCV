import cv2
import numpy as np
import requests

# Replace this with the actual IP of your ESP32-CAM
ESP32_CAM_URL = "http://192.168.1.106/cam-hi.jpg"

# HSV range for red (you can adjust or use trackbars to fine-tune)
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

while True:
    try:
        # Get the JPEG image from ESP32-CAM
        response = requests.get(ESP32_CAM_URL, timeout=2)
        img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if frame is None:
            print("Failed to decode image")
            continue

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create mask for red color (split due to HSV wraparound)
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 | mask2

        # Clean the mask
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(largest)

            if radius > 10:
                center = (int(x), int(y))
                cv2.circle(frame, center, int(radius), (0, 255, 0), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
                cv2.putText(frame, f"Ball at ({int(x)}, {int(y)})", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        else:
            cv2.putText(frame, "Ball not found", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv2.imshow("ESP32-CAM Ball Tracker", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break

    except requests.exceptions.RequestException as e:
        print(f"Failed to get image: {e}")

cv2.destroyAllWindows()
