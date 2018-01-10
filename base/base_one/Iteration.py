for i in range(1,101):
    if i%7==0:
        print i,
print '\n'
L = ['Adam', 'Lisa', 'Bart', 'Paul']
P =[1,2,3,4]
print zip(P,L)
for index, name in zip(P,L):
    print index, '-', name
# dict's value use .values()
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for i in d.values():
    sum+=i
print sum/len(d)
# dict's key and value use .items()
sum = 0.0
for k, v in d.items():
    sum = sum + v
    print k,":",v,
print 'average', ':', sum/len(d)