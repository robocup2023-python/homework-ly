import math
class Point:
    x:float
    y:float
    z:float
    def __init__(self,x:float,y:float,z:float=0) -> None:
        self.x=x
        self.y=y
        self.z=z
        print('创建了Point({},{},{})'.format(self.x,self.y,self.z))
        pass
    def __str__(self) -> str:
        return 'Point({},{},{})'.format(self.x,self.y,self.z)
    def __delattr__(self, __name: str) -> None:
        print('删除了Point({},{},{})'.format(self.x,self.y,self.z))
        pass
    def __add__(self,other):
        if(type(other)==Point):
            raise TypeError("Error 発生")
        if(type(other)==Vector):
            return Point(self.x+other.x,self.y+other.y,+self.z+other.z)
    def __sub__(self,other):
        if(type(other)==Vector):
            return Point(self.x-other.x,self.y-other.y,self.z-other.z)
        if(type(other)==Point):
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
    def __eq__(self, __value: object) -> bool:
        if(self.x==__value.x and self.y==__value.y and self.z==__value.z):
            return True
        else:
            return False
        pass
    def __lt__(self,other) -> bool:
        x1 = self.x**2+self.y**2+self.z**2
        x2= other.x**2+other.y**2+other.z**2
        if(x1==x2):
            return True
        else:
            return False
class Vector:
    x:float
    y:float
    z:float
    def __init__(self,x:float,y:float,z:float=0) -> None:
        self.x=x
        self.y=y
        self.z=z
        pass
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y,+self.z+other.z)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
    def __lt__(self,other) -> bool:
        x1 = self.x**2+self.y**2+self.z**2
        x2= other.x**2+other.y**2+other.z**2
        if(x1==x2):
            return True
        else:
            return False
    def __mul__(self,other):#旋转轴没给啊..
        x = math.radians(other)
        s = math.sin(x)
        c = math.cos(x)
        return Vector(self.x*c-self.y*s,self.x*s+self.y*c,self.z)
    def __truediv__(self,other):#旋转轴没给啊..
        x = math.radians(other)
        s = math.sin(x)
        c = math.cos(x)
        return Vector(self.x*c+self.y*s,-self.x*s+self.y*c,self.z)