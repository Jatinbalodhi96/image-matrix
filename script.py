import cv2
import sys
import os

filename = sys.argv[1]
path = os.path.dirname(os.path.abspath(__file__))
file, ext = os.path.splitext(path+ "\\" +sys.argv[1])
try:
    os.mkdir(file)
except:
    pass

img = cv2.imread(filename)

edged = cv2.Canny(img, 10, 250)#creating edged image
#cv2.imshow("Edges", edged)
cv2.waitKey(0)
img1 = img.copy()
img2 = img.copy()   

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilate = cv2.morphologyEx(edged, cv2.MORPH_GRADIENT, kernel)  #Morphological Dilation to thicken the white edges
#cv2.imwrite('dilate.jpg',dilate)
#cv2.imshow('dilate', dilate)
#cv2.waitKey(0)

_, contours, hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  #finding contours
#cv2.imwrite('fin contours.jpg',img2)
os.chdir(file)
i = 0
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)#bounding in rectangle
    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
    crop_img = img1[y:y+h, x:x+w]
    cv2.imwrite('Image_00' + str(i+1) + ext, crop_img)
    i = i + 1

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Executed! Check the directory")