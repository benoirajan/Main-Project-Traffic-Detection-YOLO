import cv2
import os

from progress import getProgress


def drawBboxAndsave(file, savedir, show=True, color=(0, 255, 0), thickness=1, dir_name='1920_1080'):
    '''
    @param file: source
    '''
    dir_name = dir_name+'/'
    img = './VehicleR/images/'+dir_name+file
    lbl = './VehicleR/labels/'+dir_name + \
        ('.'.join(file.split('.')[:-1])+'.txt')

    image = cv2.imread(img)

    height, width, channels = image.shape

    # load txt file
    label = open(lbl, 'r')
    line = label.readline()
    while line != '':
        sp = line.split()

        # class, x_center, y_center, width, height.
        x = width*float(sp[1])
        y = height*float(sp[2])
        w = float(sp[3])*width
        h = float(sp[4])*height

        p1 = (int(x-w/2), int(y-h/2))
        p2 = (int(p1[0]+w), int(p1[1]+h))

        # print(p1,p2,sp[0])

        image = cv2.rectangle(image, p1, p2, color, thickness)
        image = cv2.putText(image, sp[0], (int(x), int(
            y)), cv2.FONT_HERSHEY_COMPLEX, 0.3, color=color)

        line = label.readline()

    label.close()

    # import os
    # os.mkdir('./bbox/')
    if show:
        cv2.imshow('image', image)
        cv2.waitKey(0)
    cv2.imwrite(savedir+file, image)


if (__name__ == '__main__'):
    # file = 'val/'
    file = ''
    imgdir = "./VehicleR/images/"+file
    savedir = "./bbox vehicleR/"
    if not os.path.exists(savedir):
        os.mkdir(savedir)

    dirs = os.listdir(imgdir)
    lendirs = len(dirs)
    i = 0
    for dir in dirs:
        i += 1
        print(getProgress(i, lendirs, 100), end='')
        drawBboxAndsave(dir, savedir, False, dir_name=file)
    print()
    print('File saved to', savedir)
