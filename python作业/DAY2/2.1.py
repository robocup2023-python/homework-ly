zifu=input('输入一行字符')
num=0
char=0
space=0
other=0
for i in zifu:
    if i.isalpha():
        char+=1
    elif i.isdigit:
        num+=1
    elif i.isspace:
        space+=1
    else:
        other+=1
print('字母数为'+str(char)+'数字数为'+str(num)+'空格数为'+str(space)+'其他数字为'+str(other))