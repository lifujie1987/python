class SchoolMember(object):
    member_nums=0
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.enroll()   #初始化实例的时候，直接调用注册的方法
    def enroll(self):
        SchoolMember.member_nums +=1
        print('\033[32;1m[%s]SchoolMember [%s] is enrolled\033[0m' % (SchoolMember.member_nums,self.name))
    def tell(self):
        print('my name is [%s]'%self.name)

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,course,salary):
        super(Teacher,self).__init__(name,age,sex)
        self.course=course
        self.salary=salary
    def teaching(self):
        print('Teachen [%s] is teaching[%s]'%(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,course,tuition):
        super(Student,self).__init__(name,age,sex)
        self.course=course
        self.tuition=tuition


    def pay_tuition(self):
        print('[%s]正在缴费'%self.name)

t1=Teacher('Alex',22,'F','python',100)
t2=Teacher('Wutenglan',23,'F','python',900)

s1=Student('lifujie',29,'F','python',15000)
s2=Student('sevenbaby',30,'W','python',10000)

t1.tell()
t1.teaching()
t2.tell()
s1.tell()
s1.pay_tuition()
s2.tell()
