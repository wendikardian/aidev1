from pre_process.face_blurring import anon_face_pixelate
from pre_process.face_blurring import anon_face_simple
import numpy as np
import argparse
import cv2
import os
import time
import imutils
from imutils.video import VideoStream


ap = argparse.ArgumentParser()
ap.add_argument('-f', '--face', help="image ")
ap.add_argument('-m', '--method', type=str,default="simple", choices=["simple", "pixelated"], help="Face ")
ap.add_argument('-b', '--blocks', type=int, default=20)
ap.add_argument('-c', '--confidence', type=float, default=0.5)
args = vars(ap.parse_args())


print("[INFO] Loading Face detector model ...")
prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt.txt"])
weightsPath = os.path.sep.join([args["face"], "res10_300x300_ssd_iter_140000.caffemodel"])

net = cv2.dnn.readNet(prototxtPath, weightsPath)
print("[INFO] starting video stream ...  ")
vs = VideoStream(src = 0).start()
time.sleep(0)


while True:
    frame = vs.read()
    frame = imutils.resize(frame, width = 400)

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300,300)), 1.0, (300,300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):
        confidence = detections[0,0,i, 2]
        if confidence >  args["confidence"]:
            box = detections[0,0,i, 3:7] * np.array([w,h,w,h])
            (startX, startY, endX, endY) =box.astype("int")

            face = frame[startY: endY, startX : endX]

            if args["method"] == "simple":
                face = anon_face_simple(face, factor = 3.0)
            else:
                face = anon_face_pixelate(face, blocks = args["blocks"])
            
            frame[startY: endY, startX :  endX] = face
    
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destryAllWindows()
vs.stop()


