def a(n):
    if n==1 or n==2:
        return 1
    else:
        return a(n-1)+a(n-2)
for i in range(1,21):
    print(a(i))