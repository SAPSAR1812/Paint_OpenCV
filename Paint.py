import cv2
import numpy as np
import statistics 

e1=cv2.getTickCount()
img=cv2.imread('One.jpg')
img1=img.copy()
drawing=False
mode=True
def draw(event,x,y,flags,param):
    global ix,iy,drawing,mode
    
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.rectangle(img1,(ix,iy),(x,y),(255,0,0),5)
        else:
            r=np.round(np.sqrt((x-ix)*(x-ix)+(y-iy)*(y-iy)))
            cv2.circle(img1,(ix,iy),int(r),(0,255,0),-1)
        

img1 = np.zeros((512,512,3), np.uint8)    
cv2.namedWindow('image')  
cv2.setMouseCallback('image',draw)


while(1):
    cv2.imshow('image',img1)
    k=cv2.waitKey(1)
    if k==ord('m'):
        mode=not mode
    elif k==ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
