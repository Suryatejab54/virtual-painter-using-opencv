import cv2
import numpy as np
import time
import os
import handtracking as htm

####
brushThickness=15
eraserThickness=100



folderpath="images"
mylist=os.listdir(folderpath)
#print(mylist)
overlaylist=[]

for impath in mylist:
    image=cv2.imread(f'{folderpath}/{impath}')
    overlaylist.append(image)
#print(len(overlaylist))
header=overlaylist[0]
drawColor=(0,0,255)


cap=cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 600)

detector=htm.handDetector(detectionCon=0.85)
xp,yp=0,0
imgCanvas=np.zeros((720,1280,3),np.uint8)

while True:
    #1.
    success,img=cap.read()
    img=cv2.flip(img,1)
    #2.
    img=detector.findHands(img)
    lnlist=detector.findPosition(img,draw=False)
    
    if len(lnlist)!=0:
        #print(lnlist)
        
        x1,y1=lnlist[8][1:]
        x2,y2=lnlist[12][1:]

        #3.
        fingers=detector.fingersUp()
        #print(fingers)
        #4.
        if fingers[1] and fingers[2]:
            xp,yp=0,0
            #print("selection mode")
            if y1<125:
                if 250<x1<450:
                    header=overlaylist[0]
                    drawColor=(0,0,255)
                elif 550<x1<750:
                    header=overlaylist[1]
                    drawColor=(0,255,0)
                elif 880<x1<950:
                    header=overlaylist[2]
                    drawColor=(255,0,255)
                elif 1050<x1<1200:
                    header=overlaylist[3]
                    drawColor=(0,0,0)
            cv2.rectangle(img,(x1,y1-25),(x2,y2+25),drawColor,cv2.FILLED)

        #5.
        if fingers[1] and fingers[2]==False:
            cv2.circle(img,(x1,y1),15,drawColor,cv2.FILLED)
            #print("drawing mode")
            if xp==0 and yp==0:
                xp,yp=x1,y1
            
            if drawColor==(0,0,0):
                 cv2.line(img,(xp,yp),(x1,y1), drawColor,eraserThickness)
                 cv2.line(imgCanvas,(xp,yp),(x1,y1), drawColor,eraserThickness) 
            else:
               cv2.line(img,(xp,yp),(x1,y1), drawColor,brushThickness)
               cv2.line(imgCanvas,(xp,yp),(x1,y1), drawColor,brushThickness)

            xp,yp=x1,y1

    imgGray=cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)
    _, imgInv =cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
    imgInv=cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img=cv2.bitwise_and(img,imgInv)
    img=cv2.bitwise_or(img,imgCanvas)
    
    img[0:125, 0:1288]=header
    
    cv2.imshow("image",img)
    #cv2.imshow("Canvas",imgCanvas)
    cv2.waitKey(1)



