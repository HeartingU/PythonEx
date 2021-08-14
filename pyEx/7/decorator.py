"""
decorator:装饰器
是一个特殊的闭包函数
这个函数是给其他函数添加功能的
软件维护需要遵循开放封闭原则
    软件对扩展功能是开放的
装饰器不能改变被装饰对象的源代码
装饰器不能改变被修饰对象的调用方式
"""

name = 'dahai'


def run(n):
    print('==============')
    print('我是%s' % n)
    print('===========')


run(name)


def decorate(func):
    def new_func(name):
        print("我是装饰器前面的代码")
        func(name)
        print("我是装饰器后面的代码")

    return new_func


# 定义了new_func(name)函数； 返回了new_func内存地址；传入了一个run函数
a = decorate(run)
print(a)
a(name)
decorate(run)(name)

# 测试for循环从1到9000000的时间
n = 9000000


def for1(n):
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += i
    print(sum1)


for1(n)
from datetime import datetime


# 定义一个时间装饰器

def run_time(func):
    def new_func(*args,**kwargs): #可装饰无参数或有参数
        start_time = datetime.now()
        print('开始时间：%s' % start_time)
        func(*args,**kwargs)
        end_time = datetime.now()
        print('结束时间：%s' % end_time)
        time1 = end_time - start_time
        print('花费时间:%s' % time1)

    return new_func


run_time(for1)(n)
for1 = run_time(for1)
for1(n)


@run_time #直接装饰下面的函数
def run(n):
    print(n)
    print('run')


run(10)
