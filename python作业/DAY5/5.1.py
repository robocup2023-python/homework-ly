def cacluate(*num):
    avg = sum(num)/len(num)
    ind = []
    for n in num :
        if(n>avg):
            ind.append(num.index(n))
    a = (avg,ind)
    return a