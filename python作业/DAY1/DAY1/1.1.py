a=range(1,5)
for b in a:
    for c in a:
        for d in a:
            if d!=b and b!=c and d!=c:
                print(100*b+10*c+d)