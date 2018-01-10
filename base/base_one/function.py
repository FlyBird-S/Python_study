import math
#define function
def square_of_sum(List):
    sum_1=0
    for sum_2 in List:
        sum_1+=sum_2*sum_2
    return sum_1
print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])
# multi return is return a tuple
def quadratic_equation(a, b, c): #
    de=b*b-4*a*c
    return (-b+math.sqrt(de))/(2*a),(-b-math.sqrt(de))/(2*a)
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)
def funct(x):
    if x==1:
        return 1
    else:
        return funct(x-1)+x
print funct(3)
# function's default value
def test(a,b=2):
    return a+b
print test(1,3),test(1)
#not constant intput number
def average(*args,**kw):
    if len(args)!=0:
        return sum(args)/float(len(args))
    else:
        return 0.0
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)