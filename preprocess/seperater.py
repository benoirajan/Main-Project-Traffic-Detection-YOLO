import shutil
from PIL import Image
import os

sizeDict = {}
imgdir = "./images/val/"
dirs = os.listdir(imgdir)

for dir in dirs:
    im = Image.open(imgdir+dir)
    (a,b) = im.size
    maxnum = max(a,b)
    strs = str(a)+'_'+str(b)
    newdir = "./labels/val"+strs
    # if(maxnum == 1280 and strs == '1280_720'):
    if(strs == '1920_1080'):
        print(im.size)
        # txtname = dir
        txtname = ".".join(dir.split('.')[0:-1])+".txt"
        src = "./labels/val/"+txtname

        if(strs in sizeDict):
            sizeDict[strs]+=1
            shutil.copy(src,newdir+"/")
        else: 
            os.mkdir(newdir)
            shutil.copy(src,newdir+"/")
            sizeDict[strs] = 1

print(sizeDict)

'''
{
960: 30,
4096: 67, 
4160: 49,
1280: 355, 
640: 232, 
1920: 1144, 
854: 227,
4032: 82, 
1125: 32, 
1906: 81}
'''