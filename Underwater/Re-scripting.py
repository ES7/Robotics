import numpy as np 
import cv2
import cv2.aruco as aruco
import imutils
import math


la = [cv2.imread('Ha.jpg'),cv2.imread('HaHa.jpg'),cv2.imread('LAMO.jpg'),cv2.imread('XD.jpg')]
lid = []
lnew = {}

img = cv2.imread('CVTask.png') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
_, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

def findArucoMarkers(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_5X5_250')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    corners, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters=arucoParam)
    return (corners, ids, rejected)

for i in la:
    (corners, ids, reject) = findArucoMarkers(i)
    lid.append(corners)
    name = str(ids)
    cv2.imwrite(f"{name}.jpg", i)
    lnew.update({str(ids) : cv2.imread(f"{name}.jpg")}) #replacing img names with IDs
print(lnew.keys())

def arucocoordinates(img):
    (c,i,r) = findArucoMarkers(img)
    if len(c)> 0:
        i = i.flatten()
        for (markercorner,markerid) in zip(c,i):
            corner = markercorner.reshape((4,2))
            (tl,tr,br,bl) = corner
            tl = (int(tl[0]),int(tl[1]))
            tr = (int(tr[0]),int(tr[1]))
            bl = (int(bl[0]),int(bl[1]))
            br = (int(br[0]),int(br[1]))
        return tl,tr,br,bl

def cropimg(img):
    tl,tr,br,bl = arucocoordinates(img)
    ci = img[tl[0]:br[0], tl[1]:br[1]]
    return ci

def fixaruco(img):
    tl, tr, br, bl = arucocoordinates(img)
    m = (tl[1] - tr[1])/(tl[0] - tr[0])
    theta = math.degrees(math.atan(m))
    rimg = imutils.rotate_bound(img, -theta)
    cimg = cropimg(rimg)
    return cimg

def findColor(value):
    if (value[0]<1 and value[1]<1 and value[2]<1 and value[0]>=0 and value[1]>=0 and value[2]>=0):
        return 3, '[[3]].jpg'
    if (value[0]<250 and value[1]<250 and value[2]<250 and value[0]>200 and value[1]>200 and value[2]>200):
        return 4, '[[4]].jpg'
    if (value[0]<20 and value[1]<150 and value[2]<250 and value[0]>0 and value[1]>100 and value[2]>200):
        return 2, '[[2]].jpg'
    if (value[0]<100 and value[1]<250 and value[2]<200 and value[0]>60 and value[1]>200 and value[2]>100):
        return 1, '[[1]].jpg'
    else:
        return None


for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    i = 0

    if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h

        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            
            angle = math.degrees(math.atan((approx[2][0][1]-approx[1][0][1])/(approx[2][0][0]-approx[1][0][0])))
            
            dx = int(math.sqrt(((approx[0][0][1]-approx[1][0][1])**2)+((approx[0][0][0]-approx[1][0][0])**2)))
            dy = int(math.sqrt(((approx[2][0][1]-approx[1][0][1])**2)+((approx[2][0][0]-approx[1][0][0])**2)))
            
            col = img[int(y+(h/2)), int(x+(w/2))]

            a,b = findColor(col)
            if a==1:
                cv2.drawContours(img,[contour],0,(0,0,0),-1)
                aru = cv2.resize(fixaruco(cv2.imread(b)),(dx,dy))
                aru = imutils.rotate_bound(aru,angle+90)
                img[y:y+h-2,x:x+w-2] = img[y:y+h-2,x:x+w-2] + aru      
            
            elif a==2:
                cv2.drawContours(img,[contour],0,(0,0,0),-1)
                aru = cv2.resize(fixaruco(cv2.imread(b)),(dx,dy))
                aru = imutils.rotate_bound(aru,angle-90)
                img[y:y+h-2,x:x+w-2] = img[y:y+h-2,x:x+w-2] + aru

            elif a==3:
                cv2.drawContours(img,[contour],0,(0,0,0),-1)
                aru = cv2.resize(fixaruco(cv2.imread(b)),(dx,dy))
                aru = imutils.rotate_bound(aru,angle+90)
                img[y:y+h-1,x:x+w-3] = img[y:y+h-1,x:x+w-3] + aru

            elif a==4:
                cv2.drawContours(img,[contour],0,(0,0,0),-1)
                aru = cv2.resize(fixaruco(cv2.imread(b)),(dx,dy))
                aru = imutils.rotate_bound(aru,angle+90)
                img[y:y+h-2,x:x+w-2] = img[y:y+h-2,x:x+w-2] + aru
            else:
                pass
            

            cv2.imshow("bimg",img)
            
            
cv2.imwrite("final.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
