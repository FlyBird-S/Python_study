L = range(1, 101) #l[x:y:z]函数指的是‘开始元素’：‘最后元素’：‘取元素间隔；
print L[0:10]
print L[2::3]
print L[4:50:5]
print L[-10:]
print L[4::5][-10:]
def firstCharUpper(s):
    return s[:1].upper()+s[1:]

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')