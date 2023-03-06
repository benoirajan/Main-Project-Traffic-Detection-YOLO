import shutil
from PIL import Image
import os


imgdir = "vit ds/images/val/"
savedir = "vit ds/resize_val/"
dirs = os.listdir(imgdir)

os.mkdir(savedir)
ims = []

for dir in dirs:
    im = Image.open(imgdir+dir)
    (a, b) = im.size
    rsim = None
    if a > b:
        c = a / 640
        rsim = im.resize((640, int(b/c)))
    else:
        c = b / 640
        rsim = im.resize((int(a/c), 640))

    ims.append(rsim)
    # rsim.save(savedir+dir)

print("images resized")

for i in range(len(ims)):
    ims[i].save(savedir+dirs[i])

print("Saved")
