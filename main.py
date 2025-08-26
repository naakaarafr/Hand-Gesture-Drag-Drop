import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np
import math
import time

# Simple camera initialization
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Using DirectShow on Windows
if not cap.isOpened():
    cap = cv2.VideoCapture(0)  # Fallback to default

# Give camera time to warm up
time.sleep(2)

# Test camera
ret, test_frame = cap.read()
if not ret or test_frame is None:
    print("Camera test failed. Trying alternative method...")
    cap.release()
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Linux
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

class DragRect():
    def __init__(self, posCenter, size=[200, 200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # If the index finger tip is in the rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and \
                cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor

rectList = []
for x in range(5):
    rectList.append(DragRect([x * 250 + 150, 150]))

print("Starting camera loop. Press 'q' to quit...")

while True:
    try:
        success, img = cap.read()
        
        if not success:
            print("No frame received, skipping...")
            continue
            
        if img is None or img.size == 0:
            print("Empty frame, skipping...")
            continue
        
        # Ensure image is valid
        if len(img.shape) != 3:
            print("Invalid image format")
            continue
            
        img = cv2.flip(img, 1)
        
        # Process hands
        hands, img = detector.findHands(img)
        
        if hands:
            hand1 = hands[0]
            lmList = hand1["lmList"]
            
            # Calculate distance between fingers
            x1, y1 = lmList[8][0], lmList[8][1]  # Index finger tip
            x2, y2 = lmList[12][0], lmList[12][1]  # Middle finger tip
            
            length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            
            if length < 50:
                cursor = [lmList[8][0], lmList[8][1]]
                for rect in rectList:
                    rect.update(cursor)

        # Draw rectangles
        imgNew = np.zeros_like(img, np.uint8)
        for rect in rectList:
            cx, cy = rect.posCenter
            w, h = rect.size
            cv2.rectangle(imgNew, (cx - w // 2, cy - h // 2),
                          (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
            cvzone.cornerRect(imgNew, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)

        # Blend images
        out = img.copy()
        alpha = 0.5
        mask = imgNew.astype(bool)
        out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]

        cv2.imshow("Drag & Drop", out)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    except Exception as e:
        print(f"Error in main loop: {e}")
        continue

cap.release()
cv2.destroyAllWindows()
print("Program ended.")