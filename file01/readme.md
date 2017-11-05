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

# 类的高级用法
* 面向对象是一种编程方式，此编程方式的实现是基于对 类 和 对象 的使用
* 类 是一个模板，模板中包装了多个“函数”供使用（可以讲多函数中公用的变量封装到对象中）
* 对象，根据模板创建的实例（即：对象），实例用于调用被包装在类中的函数
* 面向对象三大特性：封装、继承和多态

## 本篇将详细介绍Python 类的成员、成员修饰符、类的特殊成员。
**类的成员可以分为三大类：字段、方法和属性**
http://images2015.cnblogs.com/blog/425762/201509/425762-20150916222236164-249943282.png

#反射
hasattr // 通过字符串来访问内存
```
if hasattr(self,'string'):
    getattr()
```
