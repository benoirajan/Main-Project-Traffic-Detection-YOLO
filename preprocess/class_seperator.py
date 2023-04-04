import os
import cv2

def drawBboxAndsave(file,savedir,show=True):
    img = './tiv ds/images/1920_1080/'+file
    lbl = './tiv ds/labels/1920_1080/'+('.'.join(file.split('.')[:-1])+'.txt')


    image = cv2.imread(img)

    height, width, channels = image.shape
    color = (0,255,0)
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

        #rectangle
        image = cv2.rectangle(image,p1,p2,color,thickness)
        # Text
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






cls = ['ambulance', 'army vehicle', 'auto rickshaw', 'bicycle', 'bus', 'car', 'garbagevan', 'human hauler', 'minibus', 'minivan', 'motorbike', 'pickup', 'policecar', 'rickshaw', 'scooter', 'suv', 'taxi', 'three wheelers -CNG-', 'truck', 'van', 'wheelbarrow']
file = '1920_1080/'
lbldir = "./tiv ds/labels/"+file
imgdir = "./tiv ds/images/"+file
savedir = "./"+file
if not os.path.exists(savedir):
    os.mkdir(savedir)
dirs = os.listdir(lbldir)
labdic = {}
print(len(dirs))
for dir in dirs:
    label = open(lbldir+dir,'r')

    # lineList = []
    clist = [0 for _ in range(21)]
    
    # print(dir)
    line = label.readline() 
    while len(line)>0:
        sp = line.split()
        index = int(sp[0])

        if index in labdic.keys():
            if clist[index] == 0:
                labdic[index].append(dir)
                clist[index] = 32
        else:
            labdic[index] = [dir]

        # sp[0]='0'
        # lineList.append(' '.join(sp))
        line = label.readline()

    label.close()
    # out = open(savedir+dir,'w')
    # out.write('\n'.join(lineList))
    # out.close()
    # if True:
    #     break
    
for key in labdic.keys():
    print(cls[key]+',','',end='')
print()
sdfs=list(labdic.keys())
sdfs.sort()
for key in sdfs:
    sd=savedir+'/'+cls[key]+'/'
    if not os.path.exists(sd):
        os.mkdir(sd)
    print(key,':',len(labdic[key]))
    for val in labdic[key]:
        f = ('.'.join(val.split('.')[:-1])+'.jpg')
        # shutil.copy(imgdir+f,sd)
        drawBboxAndsave(f, sd, False)
        


print(sdfs)
# print(labdic)

