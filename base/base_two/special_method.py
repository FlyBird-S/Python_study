#__str__ and __repr__
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def __str__(self):
        return '(Student: %s, %s, %d )'%(self.name,self.gender,self.score)
    __repr__ = __str__
s = Student('Bob', 'male', 88)
print s
#__cmp__
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__
    def __cmp__(self, s):
        if self.score > s.score:
            return -1
        elif self.score < s.score:
            return 1
        else:
            return cmp(self.name.lower(),s.name.lower())

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)
# __len__
class Fib(object):

    def __init__(self, num):
        if num > 2:
            self.num = [0,1]
            num_buff=1
            last_num_buff = 0
            for i in range(0, num-2):
                num_buff = num_buff+last_num_buff
                self.num.append(num_buff)
                last_num_buff = self.num[i+1]
    def __str__(self):
        return str(self.num)
    def __len__(self):
        return len(self.num)

f = Fib(10)
print f
print len(f)
## __math_
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)
    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)
    __repr__ = __str__


r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2
print '#------------type change'
# type change
class Rational_one(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __int__(self):
        return self.p // self.q
    def __float__(self):
        return self.p/ float(self.q)
print int(Rational_one(6,4))
print float(Rational_one(7, 2))
print float(Rational_one(1, 3))

print '#----@property'
#----@property
class Student_two(object):
    __slots__ = ('name', 'gender', '__score')
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
    @property
    def grade(self):
        if self.score >= 80:
            return  "A"
        if self.score >= 60:
            return  "B"
        if self.score < 60 :
            return  "C"

s = Student_two('Bob', 59)
print s.grade
s.score = 60
print s.grade
s.score = 99
print s.grade
###s.dasdasdppt = 1  __slots__ = ('name', 'gender', 'score') restrict element
##print s.dasdasdppt
print "#__slots__------------"
# __slots__
class Person_three(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student_three(Person_three):

    __slots__ = ('name', 'gender','score')

    def __init__(self, name, gender , score):
        Person_three.__init__(self, name, gender)
        self.score = score

s = Student_three('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score

print "#--------------__call__"
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __call__(self, friend):
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend

p = Person('Bob', 'male')
p('Tim')

class Fib_two(object):
    def __call__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        return L

f = Fib_two()
print f(10)