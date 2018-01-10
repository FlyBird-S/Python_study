import time,functools
print time.asctime( time.localtime(time.time()) ) # get time
#input function output new function
def change_funct(f):
    def f_1(*args): #not constant input number
        print "change"
        return f(*args)
    return f_1
@change_funct # add=change_funct(add)
def add(x, y, f):# input funct_name
    return f(x) + f(y)
print add(-1,2,abs)

def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

## have input decorator
def performance(unit):
    def log_decorator(f):
        def f_1(*args):
            print unit,'call '+f.__name__+'() in' , time.asctime( time.localtime(time.time()) )
            return f(*args)
        return f_1
    return log_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

# prevent function name change
def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)  # prevent function name change
        def wrapper(*args, **kw):
            return f(*args, **kw)
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial.__name__

#-------functools.partial-----
print int('0011',2)
def int2(x, base=2):
    return int(x, base)
print int2('0011')
int3=functools.partial(int,base=2)
print int3("1100")

def cmp_ignore_case(s1, s2):
    if s1.lower()>s2.lower():
        return 1
    if s1.lower()<s2.lower():
        return -1
    return 0


def cmp_ignore_case(s1, s2):
    if s1.lower() > s2.lower():
        return 1
    if s1.lower() < s2.lower():
        return -1
    return 0
sorted_ignore_case = functools.partial(sorted, cmp=cmp_ignore_case)
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])