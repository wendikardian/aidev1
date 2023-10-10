import cv2

image = cv2.imread('totoro.jpg')
image = cv2.resize(image, (500,500))


cv2.imshow("Frame", image)
kernelSizes = [(3,3) , (9,9) , (15,15)]

for k in (3, 9, 15): 
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Median {}".format(k), blurred)


cv2.waitKey(0)
cv2.destroyAllWindows()