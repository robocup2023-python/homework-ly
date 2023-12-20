i=10
height=100
while i>0:
    height=height+100*0.5**i
    i-=1
print('共经过'+str(height)+'m')
print('第十次弹起高度为'+str(100*(0.5)**10))
