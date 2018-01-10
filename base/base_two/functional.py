import math
def add(x, y, f):# input funct_name
    return f(x) + f(y)
print add(25, 9, math.sqrt)
#list map(funct,list)
def format_name(s):
   return s*s
print map(format_name, [1,2,3,4])

def format_name(s): #capitalize() title()
    return s[0].upper()+s[1:].lower()
print "das da".capitalize(),"wwww ddd".title()
print map(format_name, ['adam', 'LISA', 'barT'])
print '#--------------------- reduce()--------------------------------#'
#--------------------- reduce()--------------------------------#
PP=[2, 4, 5, 7, 12]
def prod(x, y):
    return x*y
print reduce(prod, [2, 4, 5, 7, 12])
#--------------------- filter()--------------------------------#
def is_odd(x):
    return x % 2 == 1
print filter(is_odd, [1, 4, 6, 7, 9, 12, 17])
def is_not_empty(s):
    return s and len(s.strip()) > 0
print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
def is_sqr(x):
   return math.sqrt(x)%1==0
print filter(is_sqr, range(1, 101))

#--------------------- sorted()--------------------------------#
def cmp_ignore_case(s1, s2):
    if s1.lower()>s2.lower():
        return 1
    if s1.lower()<s2.lower():
        return -1
    return 0
test=['bob', 'about', 'Zoo', 'Credit']
test.sort()
print test
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
print sorted(['bob', 'about', 'Zoo', 'Credit'], lambda x,y: cmp(x.lower(),y.lower()))
#--------------------- return function
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum
f = calc_sum([1, 2, 3, 4])
print f()
#--------------------- Closure function can avoid be other use
def count():
    fs = []
    for i in range(1, 4):
        def f(x=i):
            return x*x
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()
#---------------anonymous function  :lambda(only write one  formula )
#lambda x: x * x  == def f(x): return x*x
print filter(lambda s: s and len(s.strip()) > 0 , ['test', None, '', 'str', '  ', 'END'])
print map(lambda x: x*x,[1,2,3,4,5])