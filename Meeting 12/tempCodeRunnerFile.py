
# for i in range(0, detections.shape[2]):
#     confidence = detections[0,0,i,2]
#     if confidence > min_confidence:
#         box = detections[0,0,i , 3:7] * np.array([width, height, width, height])
#         print(box)
#         (startX, startY, endX, endY) = box.astype('int')
#         text = "{:.2f}%".format(confidence  *100)
#         y = startY - 10 if startY - 10 > 10 else startY+10

#         cv2.rectangle(image, (startX, startY), (endX, endY), (0,0,255), 2)
#         cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0,0,255), 2)
