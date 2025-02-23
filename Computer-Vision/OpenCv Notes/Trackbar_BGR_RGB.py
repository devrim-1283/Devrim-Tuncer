import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512,512,3),dtype="uint8")
cv2.namedWindow("Image")

cv2.createTrackbar("Switch","Image",0,1,nothing)
cv2.createTrackbar("R","Image",0,255,nothing)
cv2.createTrackbar("G","Image",0,255,nothing)
cv2.createTrackbar("B","Image",0,255,nothing)

while True:

    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


    r = cv2.getTrackbarPos("R","Image")
    g = cv2.getTrackbarPos("G","Image")
    b = cv2.getTrackbarPos("B","Image")
    if cv2.getTrackbarPos("Switch","Image")==1:
        img[:] = [b,g,r]
    else:
        img[:] = (0,0,0)


cv2.destroyAllWindows()