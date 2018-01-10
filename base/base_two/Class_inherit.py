class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name

class Student(Person):
    def __init__(self, name, gender, score):
       # super(Student, self).__init__(name, gender)
       Person.__init__(self,name, gender)
       self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name
class Teacher(Person):

    def __init__(self, name, gender, course):
        #super(Teacher, self).__init__(name, gender)
        Person.__init__(self,name, gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name
LaoWang = Person('LaoWang','Male')
DuanFeng = Teacher('DuanFeng', 'Female', 'English')
LiMing=Student('LiMing','Male','56')
print isinstance(DuanFeng,Person)
print isinstance(DuanFeng,Student)
print isinstance(DuanFeng,Teacher)
print isinstance(DuanFeng,object)
print DuanFeng.whoAmI()
print LaoWang.whoAmI()
print LiMing.whoAmI()
print type(DuanFeng)
#print dir(DuanFeng)
print getattr(DuanFeng,'gender') # print DuanFeng.gender
print setattr(LaoWang,'gender','Unkown')# LaoWang.gender = Unkown
print LaoWang.gender

class Person_one(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for x, y in kw.items():
            setattr(self,x , y)

p = Person_one('Bob', 'Male', age=18, course='Python')
print p.age
print p.course


print '#------------multi-inherit'
#------------multi-inherit
class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a
class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        #A.__init__(self, a)
        print 'init B...'
class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        #A.__init__(self, a)
        print 'init C...'
class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        #B.__init__(self,a)
        #C.__init__(self,a)
        print 'init D...'
D_test =D(1)



