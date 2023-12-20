import os
import random
def changeName():
    ran=random.sample(range(1,100),50)
    for i in ran:
        old='./img/'+str(i)+'.png'
        new='./img/'+str(i)+'.jpg'
        os.rename(old,new)