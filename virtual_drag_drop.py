import cv2
from hand_tracking_module import HandDetector
import cvzone
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1288)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200

class DragRect():
    def __init__(self, posCenter, size = [200, 200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # If the index finger tips in the rectangle region
        if cx-w//2 < cursor[8] < cx+w//2 and cx-h//2 < cursor[8] < cx+h//2:
            cx, cy = cursor
            self.posCenter = cx, cy

rectList = []
for x in range (5):
    rectList.append(DragRect([x*250+100, 150]))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:
        l, _, _ = detector.findDistance(8, 12, img, draw=False)
        if l < 30:
            cursor = lmList[8] # Index finger tip landmark
            # Call the update here
            for rect in rectList:
                rect.update(cursor)
    
    ## Draw Solid
    # for rect in rectList:
    #     cx, cy = rect.posCenter
    #     w, h = rect.size
    #     cv2.rectangle(img, (cx - w //2, cy - h //2), (cx+w//2, cy+h//2), colorR, cv2.FILLED)
    #     cvzone.cornerRect(img, (cx - w //2, cy - h //2), w, h), 20, rt = 0)

    ## Draw Transparent
    imgNew = np.zeros_like(img, np.uint8)
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(imgNew, (cx - w //2, cy - h //2), (cx+w//2, cy+h//2), colorR, cv2.FILLED)
        cvzone.cornerRect(imgNew, (cx - w //2, cy - h //2), w, h, 20, rt = 0)

    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1-alpha, 0)[mask]

    cv2.imshow("Image", img)
    cv2.waitKey(1)

