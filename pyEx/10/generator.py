"""
生成器
    是自定义的迭代器
"""


# 函数中包含yield，调用函数不会执行体代码，会得到一个返回值，返回值是生成器对象
def func():
    print('====1====')
    # return
    yield 1
    print('====2====')
    print('====3====')


g = func()
print(g)

print(g is g.__iter__().__iter__())
res1 = next(g)
print(res1)


def func1():
    print('====1====')
    # return
    yield 1
    print('====2====')
    yield 2
    print('====3====')


g = func1()
print(g)

print(g is g.__iter__().__iter__())
# 触发函数的执行，碰到yield停下来，并将yield后的值当作本次next的结果返回
res1 = next(g)
print(res1)
res2 = next(g)
print(res2)
# 生成器一般与for连用
for i in g:
    print(i)


# 生成器：斐波那契数列,n为数量的个数
def run(n):
    i, a, b = 0, 1, 1
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


my_run = run(10)
print(my_run)
# print(list(my_run))
for i in my_run:
    print(i)
