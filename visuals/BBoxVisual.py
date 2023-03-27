import cv2
from numpy import double

'''
@param file: source
'''
def drawBboxAndsave(file,savedir,show=True):
    img = './tiv ds/images/1920_1080/'+file
    lbl = './tiv ds/labels/1920_1080/'+('.'.join(file.split('.')[:-1])+'.txt')


    image = cv2.imread(img)

    height, width, channels = image.shape
    start_point = (0,0)
    end_point = (width, height)
    color = (255,255,0)
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
    if show:
        cv2.imshow('image',image)
        cv2.waitKey(0)
    cv2.imwrite(savedir+file,image)
    print('File saved to',savedir+file)

file = 'Asraf_01_jpg.rf.b698f86713f1b28c16ecab5f4ef89edb.jpg'

drawBboxAndsave(file,'./bbox/')
