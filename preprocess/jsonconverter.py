import json
import os
import cv2

file = ''
labeldir = "./VehicleR/labels/"+file
savedir = "./"+file
# if not os.path.exists(savedir):
#     os.mkdir(savedir)
dirs = os.listdir(labeldir)

data = {}

for dir in dirs:
    label = open(labeldir+dir,'r')

    print(dir)
    imname = ('.'.join(dir.split('.')[:-1])+'.jpg')
    impath = f"./VehicleR/images/{file}{imname}"
    size = os.path.getsize(impath)
    filed = {"filename":imname, "size": size}
    image = cv2.imread(impath)
    height, width, _ = image.shape
    region = []
    line = label.readline() 
    while len(line)>0:
        sp = line.split()
        x  = width*float(sp[1])
        y = height*float(sp[2])
        w = float(sp[3])*width
        h = float(sp[4])*height

        #VIA correction
        x-=w/2
        y-=h/2

        region.append({
            "shape_attributes": {
                "name": "rect",
                "x": int(x),
                "y": int(y),
                "width": int(w),
                "height": int(h)
            },
            "region_attributes": {
                "class": f"{sp[0]}"
            }
        })
        line = label.readline()

    filed["regions"]=region
    data[f"{imname}{size}"]= filed
    label.close()
    # if True:
    #     break
    

# Specify the path and filename for the JSON file
filename = "./VehicleR/data.json"

# Write the data to the JSON file
with open(filename, "w") as file:
    json.dump(data, file, indent=2)

print(f"JSON file '{filename}' has been created.")    