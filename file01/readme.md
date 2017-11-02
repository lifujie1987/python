 # python类的学习
 ## python 和其他语言一样，类的有一个构造方法__init__ 
 本文有3个类
* 学校类
* 老师类
* 学生类

老师类和学生类都继承了学校类的name、age、sex 属性，同时也有自己的新属性。
使用方法用super方法调用老init代码如下：
```
class Teacher(School):
    def __init__(self,name,age,sex):
    super(Teacher,self).__init__(self,name,age,sex)
    
```
