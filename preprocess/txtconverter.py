import json
import cv2
import os

f = open("./dss/tddl_json.json", "r")
data = json.load(f)

file = ''
imgdir = "./VehicleR/images/"+file
savedir = "./VehicleR/New/"+file

if not os.path.exists(savedir):
    os.mkdir(savedir)

for k in data:
    v = data[k]
    filename = v['filename']
    print(filename)
    bboxes = v['regions']

    impath = f"./VehicleR/images/{file}{filename}"
    image = cv2.imread(impath)
    height, width, _ = image.shape
    lineList = []

    for box in bboxes:
        sh = box['shape_attributes']
        x = sh["x"]
        y = sh["y"]
        w = sh["width"]
        h = sh["height"]

        x += w/2
        y += h/2

        x /= width
        y /= height
        w /= width
        h /= height

        x = str(x)
        y = str(y)
        w = str(w)
        h = str(h)

        cls = str(box['region_attributes']['class'])
        # print(x,y,w,h,cls)
        lineList.append(" ".join([cls,x,y,w,h]))
    
    lblname = ('.'.join(filename.split('.')[:-1])+'.txt')
    out = open(savedir+lblname,'w')
    out.write('\n'.join(lineList))
    out.close()

    # break
