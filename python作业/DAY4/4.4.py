list=[1,2,3,4,5,6,7,8,9,10]
m=5
i=0
while i<5:
    list.insert(0,list.pop(-1))
    i+=1
print(list)