import threading, time

LOOP_MAX = 10
loop_n = 0
loop_1_n = 0
loop_2_n = threading.local()
lock = threading.Lock()


# 主线程与新线程共同作用于loop_n
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    global loop_n  # 声明为全局变量
    while loop_n < LOOP_MAX:
        loop_n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, loop_n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def loop_1():  # 上锁后一个线程操作完毕另一个才可以操作
    print('thread %s is running...' % threading.current_thread().name)
    global loop_1_n  # 声明为全局变量
    while loop_1_n < LOOP_MAX:
        try:
            lock.acquire()
            loop_1_n += 1
        finally:
            lock.release()
        print('thread %s >>> %s' % (threading.current_thread().name, loop_1_n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def loop_2(max=LOOP_MAX):  # 运用ThreadLocal给不同的线程不同的变量
    print('thread %s is running...' % threading.current_thread().name)
    loop_2_n.n = 0
    while loop_2_n.n < max:
        loop_2_n.n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, loop_2_n.n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')  # 参数（调用函数，线程名）
t.start()
loop()
t1 = threading.Thread(target=loop_1, name="test1")
t1.start()
loop_1()
t2 = threading.Thread(target=loop_2, args=(8,), name="test2")
t2.start()
loop_2(5)
t.join()
t1.join()
t2.join()
print('thread %s ended.' % threading.current_thread().name)
