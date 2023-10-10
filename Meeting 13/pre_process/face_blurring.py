import numpy as np
import cv2


def anon_face_simple(image, factor = 3.0):
    (h, w) = image.shape[:2]
    kW = int(w/factor)
    kH = int(h/factor)
    if kW%2 == 0:
        kW -= 1
    if kH %2 == 0:
        kH -= 1
    return cv2.GaussianBlur(image, (kW,  kH), 0)

def anon_face_pixelate(image, blocks = 3): 
    (h, w) = image.shape[:2]
    xSteps = np.linspace(0, w, blocks + 1, dtype = "int")
    ySteps = np.linspace(0, h, blocks + 1, dtype ="int")

    for i in range(1, len(ySteps)):
        for j in range(1, len(xSteps)):
            startX = xSteps[j - 1]
            startY = ySteps[i - 1]
            endX = xSteps[j]
            endY = xSteps[i]

            roi = image[startY : endY, startX : endX]

            (B, G, R) = [int (x) for x in cv2.mean(roi)[:3]]
            cv2.rectangle(image, (startX, startY), (endX, endY), (255,0,0) , -1)

    return image
