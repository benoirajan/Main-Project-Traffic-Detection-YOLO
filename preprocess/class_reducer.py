import os

file = '640_360/'
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


        #class value to bus
        if sp[0] in ['4','8']:
            sp[0]='0'
        elif sp[0] in ['5','9','19','12','15', '16','0']:
            sp[0]='1'
        elif sp[0] in ['7','6','11','20']:
            sp[0]='2'
        elif sp[0] in ['2','13','17']:
            sp[0]='3'
        elif sp[0] in ['1','18']:
            sp[0]='4'
        elif sp[0] in ['3','10','14']:
            sp[0]='5'

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