import cv2
from numpy import double

file = 'Asraf_06_jpg.rf.29370f9b72bb41d84fd7205a8db6ea54.jpg'

img = './tiv ds/images/1920_1080/'+file
lbl = './tiv ds/labels/1920_1080n/'+('.'.join(file.split('.')[:-1])+'.txt')


image = cv2.imread(img)



height, width, channels = image.shape
start_point = (0,0)
end_point = (width, height)
color = (255,255,255)
thickness = 1

#load txt file
label = open(lbl,'r')
line = label.readline() 
while line != '':
    sp = line.split()

    # class, x_center, y_center, width, height.
    x  = width*float(sp[1])
    y = height*float(sp[2])
    w = float(sp[3])*width
    h = float(sp[4])*height

    p1 = (int(x-w/2), int(y-h/2))
    p2 = (int(p1[0]+w), int(p1[1]+h))

    # print(p1,p2,sp[0])

    image = cv2.rectangle(image,p1,p2,color,thickness)
    image = cv2.putText(image,sp[0],(int(x),int(y)),cv2.FONT_HERSHEY_COMPLEX,0.3,color=color)

    line = label.readline()

label.close()

# import os
# os.mkdir('./bbox/')
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.imwrite('./bbox/'+file,image)