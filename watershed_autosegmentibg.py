import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import  cm

image=cv2.imread("C:/road_image.jpg")
# image=cv2.resize(image,(500,500))
image_c=image.copy()
marker_image =np.zeros(image.shape[:2],np.int32)
segment=np.zeros(image.shape,np.uint8)

c_marker=1
up_marker=False
def create_rgb(i):
    return tuple(255*(np.array(cm.tab10(i)[:3])))
colors=[]
for i in range(10):
    colors.append(create_rgb(i))

def set_mouse(event,x,y,flag,param):
    global  up_marker
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image,(x,y),10,[c_marker],-1)
        cv2.circle(image_c,(x,y),10,colors[c_marker],-1)
        up_marker=True

cv2.namedWindow('dog')
cv2.setMouseCallback('dog',set_mouse)


while True:
    cv2.imshow('segments',segment)
    cv2.imshow('dog',image_c)
    # cv2.moveWindow('dog',)
    k=cv2.waitKey(1)
    if k==27:
        break
    elif k==ord('c'):
        image_c=image.copy()
        marker_image = np.zeros(image.shape[:2], np.int32)
        segment = np.zeros(image.shape, np.uint8)
    elif k >0 and chr(k).isdigit():
        c_marker=int(chr(k))
        print(int(chr(k)))

    if up_marker:
        marker_image_copy=marker_image.copy()
        cv2.watershed(image,marker_image_copy)
        segment = np.zeros(image.shape, np.uint8)

        for color_ind in range(10):
            segment[marker_image_copy==(color_ind)]=colors[color_ind]





cv2.destroyAllWindows()