import threading
import time
import random
import os
#生成地图
class Universe():
    map = [[' ' for i in range(20)] for i in range(20)]
    def show(this):
        for i in this.map:
            print(i)
def mapReload():
    for i in cells:
        if(i.isAlive==True):
            u_main.map[i.position[1]-1][i.position[0]-1] = '*'
        else:
            u_main.map[i.position[1]-1][i.position[0]-1] = ' '
def initCell(cell):
    cell.isAlive = True
#判断周围细胞存活数
def alive(cell):
    num = 0
    x = cell.position[0]-1
    y = cell.position[1]-1
    m = u_main.map
    if(y-1>=0 and m[y-1][x]=='*'):#A
        num += 1
    if((y+1)<10 and m[y+1][x]=='*'):#D
        num += 1
    if((x-1)>=0 and m[y][x-1]=='*'):#X
        num += 1
    if((x+1)<20 and m[y][x+1]=='*'):#W
        num += 1
    if((x-1)>=0 and (y-1)>=0 and m[y-1][x-1]=='*'):#Z
        num += 1
    if((x+1)<20 and (y-1)>=0 and m[y-1][x+1]=='*'):#C
        num += 1
    if((x-1)>=0 and (y+1)<10 and m[y+1][x-1]=='*'):#Q
        num += 1
    if((x+1)<20 and (y+1)<10 and m[y+1][x+1]=='*'):#E
        num +=1
    return num
def clock():
    while(isContinue):
        time.sleep(0.5)
        #生存规则
        for i in cells:
            neighbor = 0
            neighbor = alive(i)
            if(neighbor < 2 or neighbor > 3):
                i.isAlive = False
            elif((neighbor == 2 or neighbor == 3 ) and i.isAlive == True):
                i.isAlive = True
            elif(neighbor == 3 and i.isAlive == False):
                i.isAlive = True
        mapReload()
        os.system('cls || clear')
        u_main.show()
        print('按回车键关闭...')
class Cell():
    isAlive = bool
    isAlive_next = bool
    position = (None,None)
    def __init__(self,x:int,y:int) -> None:
        self.position = (x,y)
        pass
#  迭代用线程
timer = threading.Thread(target=clock)
# 宇宙和细胞创建
u_main = Universe()
cells = []
for i in range(1,16):
    for j in range(1,20):
        cells.append(Cell(j,i))
# 激活新细胞
for i in range(1,119): 
    initCell(cells[random.randint(0,80)])
mapReload()
isContinue = True
os.system('cls || clear')
print('started')
u_main.show()
time.sleep(0.5)
timer.start()
exit = input()
isContinue = False
print('正在关闭...')
timer.join()