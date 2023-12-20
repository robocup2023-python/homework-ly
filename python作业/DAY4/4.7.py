a=list(range(1,234))
c=0
while len(a)>1:
    b=a[:]
    for i in range(0,len(b)):
        c+=1
        if c%3==0:
            a.remove(b[i])
print(a[0])