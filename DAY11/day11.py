import threading
import os
def changeName(i):
  old = './123/'+str(i)+'.txt'
  new = './123/'+str(i)+'a'+'.txt'
  os.rename(old,new)
def xc1():
  for i in range(1,101):
    if i % 2 == 1:
      changeName(i)
def xc2():
  for i in range(1,101):
    if i % 2 == 0:
      changeName(i)
t1 = threading.Thread(target=xc1)
t2 = threading.Thread(target=xc2)
t1.start()
t2.start()
t1.join()
t2.join()