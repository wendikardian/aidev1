import cv2
image = cv2.imread('totoro.jpg')

image = cv2.resize(image, (500,500))

bp = [(11,21,7), (11,41,21), (11,61,39)]

for (diameter, sigmaColor, sigmaSpace) in bp:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    title  = "Blurred  d = {}, sC = {}, sS = {}".format(diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)


cv2.imshow("Frame", image)

cv2.waitKey(0)
cv2.destroyAllWindows()