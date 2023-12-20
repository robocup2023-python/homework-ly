def qjs(*num):
    i=0
    j=[]
    while i<len(num):
        if i%2==1:
            j.append(num[i])
        i+=1
    return j
lst=[i for i in range(1,100)]