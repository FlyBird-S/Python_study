d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print d
d['Lisa']=20  #change
d['Song']=100 #add
print d

for key in d:#all show
    print key+':',d[key]


print len(d),d.__len__()
print d['Adam']
# avoid KeyError
if 'xx' in d:
    print d['xx']
print d.get('xx')
# key cannot change and repeat,value can be change 
# -*- coding: utf-8 -*-
d = {
    '123': [1, 2, 3],  # key 是 str，value是list
    123: '123',  # key 是 int，value 是 str
    ('a', 'b'): True  # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
}
print d
