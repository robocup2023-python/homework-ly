import random
import shutil
file=open('test.txt','w')
i=int(input('输入一个数字'))
while i>=1:
    file.write(chr(random.randint(32,126))+'\n')
    i-=1
file.close()
shutil.copy('test.txt','copy_test.txt')