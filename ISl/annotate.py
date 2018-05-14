import shutil,os,sys
import re
import csv
from PIL import Image
cwd= os.getcwd()
g=os.listdir(cwd)
print(g)
for i in g:
    st=str(i)
    if '.csv' in st:
        print(i)
        f=open(i,"rb")
        readcsv=csv.reader(f)
        k=0
        for j in readcsv:
            b=cwd+"/dataset/"+j[0]
            bd=cwd+"/dataset/"
            if k > 0:
                im=Image.open(b)
                x,y=im.size
                s = re.sub('\.jpg$', '.txt', b)
                d =re.sub('\_loc.csv', '', i)
                e="\\"+d
                d=re.sub(e,"",j[0])
                print(d,x,y)               
                asc=d[1]
                print str(ord(asc)-65)
                print j
                t=open(s,"wb")
                x1=int(j[1])
                x2=int(j[3])
                y1=int(j[2])
                y2=int(j[4])
                print(x1,x2,y1,y2)
                print(str(ord(asc)-65)+" "+str((x1+x2)/(2.0*x))+" "+str((y1+y2)/(2.0*y))+" "+str((-x1+x2)/(1.0*x))+" "+str((-y1+y2)/(1.0*y)))
                t.write(str(ord(asc)-65)+" "+str((x1+x2)/(2.0*x))+" "+str((y1+y2)/(2.0*y))+" "+str((-x1+x2)/(1.0*x))+" "+str((-y1+y2)/(1.0*y)))
                t.close()
                im.close()
            k=k+1
        f.close()
