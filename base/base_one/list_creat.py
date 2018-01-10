L=[]
for x in range(1,11):
    L.append(x*x)
P=[x*x for x in range(1, 11)]
print L
print P
print [i*(i+1) for i in range(1,101,2)] # [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print [x  for x in range(1, 11) if x % 2 == 0] # 2,4,6,8,10

print [i*100+j*10+k for i in range(1,10) for j in range(0,10)for k in range(0,10) if i==k] # multi for

def toUppers(L):
    return [char.upper() for char in L if isinstance(char,str)] #isinstance  type judge
print toUppers(['Hello', 'world', 101])


d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score<60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.items()]  ### key
# print '<table border="1">'
# print '<tr><th>Name</th><th>Score</th><tr>'
# print '\n'.join(tds)
# print '</table>'
L=[1,2,3,1,2,4]
L=set(L)
print L
