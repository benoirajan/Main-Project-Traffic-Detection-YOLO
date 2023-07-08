import shutil
import os

ldir = './VehicleR/'
dirs = os.listdir(ldir)
newDir = './VehicleR/sd/'
if not os.path.exists(newDir):
    os.mkdir(newDir)
for dir in dirs:
    if os.path.isfile(ldir+dir):
        shutil.copy(ldir+dir,newDir+"/"+('.'.join(dir.split('.')[:-1])+'.jpg').replace(' ','_'))