def compare(a:str,b:str) -> list :
    f1 = open(a,'r')
    f2 = open(b,'r')
    l1 = f1.readlines()
    l2 = f2.readlines()
    i = min(len(l1),len(l2))
    dif = []
    while(i>0):
        if(l1[i-1] != l2[i-1]):
            dif.append(i)
        i -= 1
    i = min(len(l1),len(l2))
    if(len(l1)!=len(l2)):
        while(i<max(len(l1),len(l2))):
            i += 1
            dif.append(i)
    dif.sort()
    return dif