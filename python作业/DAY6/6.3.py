class Person:
    name=''
    age=3
    sex=True
    def personInfo(self):
        s='男' if self.sex==True else '女' 
        print('姓名：'+self.name)
        print('年龄：'+self.age)
        print('性别：'+s)
        return
class Student(Person):
    college=''
    classRoom=''
    def personInfo(self):
        s='男' if self.sex==True else '女' 
        print('姓名：'+self.name)
        print('年龄：'+self.age)
        print('性别：'+s)
        print('学院:'+self.college)
        print('班级:'+self.classRoom)
        return
    def __str__(self):
        s='男' if self.sex==True else '女' 
        return '姓名：{} 年龄：{} 性别：{} 学院：{} 班级：{}'.format(self.name,self.age,s,self.college,self.classRoom)
