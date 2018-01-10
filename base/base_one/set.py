L=[1,2,2]
print L,"length=",len(L)
s = set(L) # set cannot repeat , the element must was constant
print s,"length=",len(s)
print 2 in s # visit
print 3 in s
for test in s:  # all show
    print test

#s.remove(test) #delete set element
#s.add(test)    #add set element

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for test in L:
    if test in s:
        s.remove(test)
    else:
        s.add(test)
print s