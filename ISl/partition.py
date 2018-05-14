import shutil,os,sys
import re
from PIL import Image
trcwd=os.getcwd()
trf=open(trcwd+'/train.txt','w')
tef=open(trcwd+'/test.txt','w')
os.chdir(os.getcwd()+'/dataset')
cwd= os.getcwd()
g=os.listdir(cwd)
c=0
for i in g:
    fold=cwd+'/'+i
    k=os.listdir(fold)
    for j in k:
        if '.jpg' in j:
            c=c+1
            c=c%4
            if c==0:
                tef.write(fold+"/"+j+'\n')
            else :
                trf.write(fold+'/' + j + '\n')
