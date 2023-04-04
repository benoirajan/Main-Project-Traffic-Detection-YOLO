import os
from visuals.progress import getProgress

file = 'val/'
imgdir = "./singlecls ds/labels/"+file
savedir = "./"+file
if not os.path.exists(savedir):
    os.mkdir(savedir)
dirs = os.listdir(imgdir)
total_r = 0
total = len(dirs)
i = 0
for dir in dirs:
    i += 1
    
    label = open(imgdir+dir, 'r')
    lineList = []
    removed = 0
    line = label.readline()
    while len(line) > 0:
        sp = line.split()

        # class, x_center, y_center, width, height.
        w = float(sp[3])
        h = float(sp[4])
        
        #removing size less than .04
        if (min(w, h) > .04):
            lineList.append(' '.join(sp))
        else:
            removed += 1
        line = label.readline()
    print(getProgress(i,total,100),total_r,end='')
    total_r += removed
    label.close()
    out = open(savedir+dir, 'w')
    out.write('\n'.join(lineList))
    out.close()
    # if True:
    #     break


print("\nTotal removed:", total_r)
