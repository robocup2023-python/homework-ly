i=input('输入一个任一位数的正整数')
weihsu=len(i)
k=[]
for h in i:
    k.append(h)
k.reverse()
print(weihsu,''.join(k))