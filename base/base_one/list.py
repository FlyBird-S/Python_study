#coding_type utf
#study list
list_1 = ["SongPengFei","first","second","third"] # 0(-4),1(-3),2(-2),3(-1)
list_2 = [ ]
print list_1
print list_1[1]
print list_1[-4]
list_1.insert(1,"new") # insert
print list_1
print list_1.__len__()
list_1.append("test")  # rear insert
print list_1.__len__()
if list_2 :
    print "true"
else:
    print "false"
print list_1
print list_1.pop() #rear delete
print list_1.pop(2) # delete
print list_1