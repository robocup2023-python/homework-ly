import random
def inssz():
    wenj='data.txt'
    f=open(wenj,'w')
    j=0
    while j<100000:
        i=int(random.random()*100+1)
        f=open(wenj,'a')
        f.write('\n'+str(i))
        f.close()
        j+=1