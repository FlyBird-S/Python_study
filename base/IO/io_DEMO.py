import time
from io import StringIO, BytesIO

# with open('test.txt', 'r') as f:  # with xx as xx 这种方式在调用前后使用 __enter__ & __exit__可以确保资源的及时释放 不必使用f.close()
#     s = f.read()
#     print(s)
# with open("test_copy.txt", 'w') as f:
#     f.write(s)

# StringIO和BytesIO 不用文件在内存中读写str和byte
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
f = StringIO('Hello!\nHi!\nGoodbye!')
print(f.read())
f = BytesIO()
f.write('西园寺世界'.encode('utf-8'))
print(f.getvalue().decode("utf-8"))

# 序列化
import pickle

student = {"name": "wang", "age": 25}
p = pickle.dumps(student)  # 序列化
print(p)
print(pickle.loads(p))  # 反序列化

import json

j = json.dumps(student)  # 序列化
print(json.loads(j))  # 反序列化
