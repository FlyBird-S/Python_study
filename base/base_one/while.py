sum = 0
x = 1
while x<=100:
    if x%2!=0:
        sum+=x
    x+=1
print sum

sum = 0
x = 1
n = 1
while True:
    sum+=x
    if n==20:
        break
    x*=2
    n+=1
print sum
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x%2==0:
        continue
    sum+=x
print sum

for x in [0,1,2,3,4,5,6,7,8,9 ]:
    for y in [ 0, 1,2,3,4,5,6,7,8,9  ]:
        if x<y:
            print x*10+y,  #if don't next line show please add ',' in rear