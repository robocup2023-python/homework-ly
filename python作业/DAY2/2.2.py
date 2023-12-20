a=int(input('bring in a number'))
n=int(input('bring in a number'))
s=0
for i in range(1,n+1):
    while i>=1:
        s=a*10**(i-1)+s
        i=1-1
print(s)