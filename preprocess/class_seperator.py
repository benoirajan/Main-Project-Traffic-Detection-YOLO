import os
import cv2

def drawBboxAndsave(file,source, savedir, key, show=True):
    img = f'./tiv ds/images/{source}/{file}'.replace('//','/')
    lbl = f"./tiv ds/labels/{source}/{('.'.join(file.split('.')[:-1])+'.txt')}".replace('//','/')

    image = cv2.imread(img)

    height, width, _ = image.shape
    color = (255,255,0)
    thickness = 2

    #load txt file
    label = open(lbl,'r')
    line = label.readline() 
    while line != '':
        sp = line.split()

        # class, x_center, y_center, width, height.
        if int(sp[0]) == key:
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
    s = (savedir+file).replace('//','/')
    cv2.imwrite(s,image)
    print('File saved to',s)






# cls = ['ambulance', 'army vehicle', 'auto rickshaw', 'bicycle', 'bus', 'car', 'garbagevan', 'human hauler', 'minibus', 'minivan', 'motorbike', 'pickup', 'policecar', 'rickshaw', 'scooter', 'suv', 'taxi', 'three wheelers -CNG-', 'truck', 'van', 'wheelbarrow']
cls = ['bus', 'car', 'other', 'three wheeler', 'truck', 'two wheeler']
file = '640_360/'
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
        drawBboxAndsave(f, file, sd, key, False)
        


# print(sdfs)
# print(labdic)
'''
ambulance 0, 
army vehicle 1, 
auto rickshaw 2, 
bicycle 3, 
'bus 4', 
'car 5', 
'garbagevan 6', 
'human hauler 7', 
'minibus 8', 
'minivan 9', 
'motorbike 10',
pickup 11', 
policecar 12', 
'rickshaw 13', 
'scooter 14', '
suv 15', 
'taxi 16', 
'three wheelers -CNG- 17', 
'truck 18', 
'van 19', 
wheelbarrow 20

'''
