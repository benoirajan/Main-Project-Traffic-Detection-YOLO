import os

file = 'val/'
imgdir = "./tiv ds/labels/"+file
savedir = "./"+file
if not os.path.exists(savedir):
    os.mkdir(savedir)
dirs = os.listdir(imgdir)
labdic = {}
for dir in dirs:
    label = open(imgdir+dir,'r')

    lineList = []
    print(dir)
    line = label.readline() 
    while len(line)>0:
        sp = line.split()
        if sp[0] in labdic.keys():
            labdic[sp[0]] += 1
        else:
            labdic[sp[0]] = 1


        #class value to 0
        sp[0]='0'
        lineList.append(' '.join(sp))
        line = label.readline()

    label.close()
    out = open(savedir+dir,'w')
    out.write('\n'.join(lineList))
    out.close()
    # if True:
    #     break
    

print(labdic.keys())
print(labdic)