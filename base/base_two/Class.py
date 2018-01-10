class Person (object):
    pass
xiaoming = Person()
xiaohong = Person()
xiaoming.age=15
xiaohong.school="high school"
print xiaoming.age
print xiaohong.school
print xiaoming == xiaohong

def cmp_1(x,y):
    if isinstance(x,str):
        return cmp(x.lower(),y.lower())
    else:
        return cmp(x,y)
print cmp_1(1,2),cmp_1('B','a'),cmp('b','a')

######################################
class Person(object):
    def __init__(self,name,gender,birth,*args,**kw):## **kw -> dict  *args -> list
        self.name = name
        self.gender = gender
        self.birth = birth
        for k, v in kw.items():
            setattr(self,k,v)
xiaoming = Person('Xiao Ming', 'Male', '1990-1-1',age=25, job='Student')
print xiaoming.name
print xiaoming.job
print xiaoming.age
# visit restrict
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
p = Person('Bob', 59)
print p.name
try:
    print p.__score
except AttributeError:
    print "__score cannot be visit"
#---------------------------------------------#
class Person(object):
    count=0
    def __init__(self,name):
        Person.count+=1
        self.name=name

p1 = Person('Bob')
print Person.count,p1.count

p2 = Person('Alice')
print Person.count,p1.count

p3 = Person('Tim')
print Person.count,p3.count

p3.count=0
print Person.count,p1.count,p3.count
del p3.count
print Person.count,p1.count,p3.count
#---------------------------------------------#
class Person(object):

    __count = 0

    def __init__(self, name):
        Person.__count += 1
        self.name = name
        print Person.__count

p1 = Person('Bob')
p2 = Person('Alice')

try:
    print Person.__count
except AttributeError:
    print 'AttributeError'

#---------private attributes
class Person(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
p1 = Person('Bob')
print p1.get_name()


class Person(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        if self.__score >= 60:
            return 'B'
        else :
            return 'C'

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()
#-------------------#
import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()
#----------------------------#

class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()
print  '#---------------------------------------#'
#---------------------------------------#
class Person(object):
    __count = 0
    @classmethod
    def how_many(cls):
        return cls.__count
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1
    def get_many(self):
        print Person.__count
print Person.how_many()
p1 = Person('Bob')
print Person.how_many()
p1.get_many()