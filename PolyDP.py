import numpy as np
import cv2

img = cv2.imread('horse1.png')
img = cv2.resize(img, None,fx=1, fy=1, interpolation = cv2.INTER_CUBIC)

canvas = 255*np.zeros(img.shape, np.uint8)
img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5),np.float32)/25
img2gray = cv2.filter2D(img2gray,-1,kernel)

ret,thresh = cv2.threshold(img2gray,250,255,cv2.THRESH_BINARY_INV)
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cnt = contours[0]
cv2.drawContours(img2gray, [cnt], 0, (0,255,0), 3)

cnt = contours[0]
max_area = cv2.contourArea(cnt)

for cont in contours:
    if cv2.contourArea(cont) > max_area:
        cnt = cont
        max_area = cv2.contourArea(cont)

perimeter = cv2.arcLength(cnt,True)
epsilon = 0.003*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

poly = []
for ele in approx:
    poly = poly + [tuple(ele[0])]

hull = cv2.convexHull(cnt)

l = len(approx)

for i in range(l):
	pa = (approx[i].item(0), approx[i].item(1))
	pb = (approx[(i+1)%l].item(0), approx[(i+1)%l].item(1))
	cv2.line(canvas, pa, pb, (255, 0, 0), 2)

cv2.drawContours(canvas, approx, -1, (0, 0, 255), 3)
	
cv2.imshow("Contour", canvas)
k = cv2.waitKey(0)

if k == 27:       
    cv2.destroyAllWindows()
