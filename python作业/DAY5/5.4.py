import os
def newFile():
    path='./img'
    os.makedirs(path)
    i=1
    while(i<=100):
        fullPath=path +'/'+ str(i)+'.png'
        file=open(fullPath,'w')
        file.close()
        i+=1