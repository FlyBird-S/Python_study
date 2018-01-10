import re
def show_file(f_name,x):
    p=open(f_name)
    for len in p:
        if len.startswith(x):
            print len
#show_file(r'imooc.txt','imooc')
#-----------------------#
str_1_1="imooc python"
pa = re.compile(r'imooc')
ma = pa.match(str_1_1)
print ma.span(),ma.string
pa = re.compile(r'imooc',re.I)
ma = pa.match("ImooC Python")
print ma.group()
ma = re.match(r'imooc','Imooc Python',re.I)
print ma.group()
#---------------one char----------------#
ma = re.match(r'..','xsw')
try :
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'{.}','{1},sda2,{4}')
try :
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'{[a-zA-Z0-9]}','{2},sda2,{4}')
try :
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'{[\w]}','{A},sda2,{4}')
try :
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'{[\W]}','{ },sda2,{4}')
try :
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'{[\d]}', '{2}')
try:
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'{\[[\d]\]}', '{[2]}')
try:
    print ma.group()
except AttributeError:
    print "Match error"

#---------------multi char----------------#
ma = re.match(r'{\d\d*}', '{3876667}')
try:
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'[A-Z][a-z]+', 'ADd')
try:
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'[A-Z][a-z]*', 'ADd')
try:
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'[1-9]?[0-9]', '86') #0-99
try:
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'[a-zA-Z0-9]{4,7}@qq.com', 'wdd22@qq.com')
try:
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'[0-9][a-z]+', '3ddd')
try:
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'[0-9][a-z]+?', '3ddd')
try:
    print ma.group()
except AttributeError:
    print "Match error"
#___________frontier matching____
ma = re.match(r'^[0-9][a-z]$', '3d')
try:
    print ma.group()
except AttributeError:
    print "Match error"
#------multi group
ma = re.match(r'abc|d', 'abc')
try:
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'abc|d', 'd')
try:
    print ma.group()
except AttributeError:
    print "Match error"

ma = re.match(r'[1-9]?\d$|100', '100')
try:
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'[\w]{4,7}@(qq|163).com', 'wdd22@163.com')
try:
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'<([\w]+>)[\w]+</(\1)', '<book>python</book>')
try:
    print ma.groups()
    print ma.group()
except AttributeError:
    print "Match error"
ma = re.match(r'<(?P<name>[\w]+>)[\w]+</(?P=name)', '<book>python</book>')
try:
    print ma.group()
    print ma.groups()
except AttributeError:
    print "Match error"
#----other re model act
str_1 = 'imooc videonum = 355'
info = re.search(r'\d{2,4}',str_1)
try:
    print info.group()
except AttributeError:
    print "Match error"
str_1_2 = 'C++=100 ,python=80 , java=90'
info = re.findall(r'\d{2,4}',str_1_2)
print info,sum(int(x) for x in info)
print sum(map(int,info))

str_1 = 'imooc videonum = 355'
info = re.sub(r'\d+','1000',str_1)
print info
def add_1(match):
    return str(int(match.group())+1)
str_1 = 'imooc videonum = 355'
info = re.sub(r'\d+',add_1,str_1)
print info

str_1 = 'imooc:C C++ Java Python,C#'
info = re.split(r':| |,',str_1)
print info