from pre_process.face_blurring import anon_face_pixelate
from pre_process.face_blurring import anon_face_simple
import numpy as np
import argparse
import cv2
import os
 
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', help="image ")
ap.add_argument('-f', '--face', help="image ")
ap.add_argument('-m', '--method', type=str,default="simple", choices=["simple", "pixelated"], help="Face ")
ap.add_argument('-b', '--blocks', type=int, default=20)
ap.add_argument('-c', '--confidence', type=float, default=0.5)
args = vars(ap.parse_args())


print("[INFO] Loading Face detector model ...")
prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt.txt"])
weightsPath = os.path.sep.join([args["face"], "res10_300x300_ssd_iter_140000.caffemodel"])

net = cv2.dnn.readNet(prototxtPath, weightsPath)

image = cv2.imread(args["image"])
orig = image.copy()

(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300,300)), 1.0, (300,300), (104, 117, 123))
net.setInput(blob)
detections = net.forward()

print("[INFO] Computing face detections ...")

for i in range(0 , detections.shape[2]):
    confidence = detections[0,0,i, 2]

    if confidence > args["confidence"]:
        box = detections[0,0,i, 3:7] * np.array([w,h, w,h])
        (startX, startY, endX, endY) = box.astype("int")
        face = image[startY : endY, startX : endX]

        if args["method"] == "simple":
            face = anon_face_simple(face, factor=3.0)
        else:
            face = anon_face_pixelate(face, blocks = args["blocks"])
        image[startY : endY, startX : endX] = face

output = np.hstack([orig, image])

cv2.imshow("Output", output)
cv2.waitKey(0)


