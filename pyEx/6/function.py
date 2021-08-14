"""
函数:具备某一功能的工具
函数的使用必须遵循函数先定义后调用的原则
不使用函数的问题：
    程序冗长
    程序的扩展性差
    可读性差
"""


# 定义函数 :
# def 函数名（）：
#   函数代码
def factory():
    print('制造手机')


# 函数调用：函数名（）
factory()


# 函数的三大特性
# 功能 参数 返回值

# 无功能函数(用来测试，写项目需求）
def shopping():
    pass


shopping()


# 参数
# 无参数应用是仅仅执行一些操作
def factory1():
    print('制造手机')


factory1()


# 有参熟需要外部传进来参数
def factory2(x, y):  # x,y为两个形参，两个变量名
    c = x + y
    print(c)


factory2(1, 2)  # 1,2是两个实参,运行的时候需要放进去,调用的时候就是把实参赋值给形参

# 关键字传参：按照key=value的形式传参,同一个key只能出现一次
# 这样可以打乱顺序传参

factory2(x=1, y=2)
factory2(y=1, x=2)
factory2(1, y=2)  # 位置传参和关键字传参混用的话只能是位置传参的放在前面，关键字传参在后面


# 默认参数:大多数传的值相同时，可以这样使用
def factory3(a, b=2):
    c = a + b
    print(c)


factory3(1)
factory3(1, 4)


# 不定长参数（可以随意放入参数）
# 在形参中带*，会将调用函数时一出位置的实参保存成元组形式。然后赋值*后的变量名
def foo(x, y, *z):
    print(x, y, z)
    print(*z)  # 拆包


foo(1, 2, 3)
foo(1, 2, 3, 4, 5, 6)

# 拆包
# 一个元素对应一个变量
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)
# 交叉赋值
a = 1
b = 2
a = b
print(a)
print(b)
# 多个元素对应一个变量
*a, b, c = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
print(c)
print(*a)


def foo1(x, y, z):
    print(x, y, z)


# *只能打散序列类型：元组，列表，字符串
foo1(1, *(2, 3))
foo1(*(1, 2, 3))
foo1(*[1, 2, 3])
foo1(*'abc')


# 形参带**:可以变为字典
def foo2(x, y, **z):
    print(x, y, z)


foo2(1, 2, a=1, b=3, c=6)


# 规范：在形参中带有*后的变量名应为args，**后的变量名应为kwargs
def factory(*args, **kwargs):
    print(args)
    print(kwargs)


factory(1, 2, 3, 4, x=5, y=8)
factory(*[1, 2.3], **{'x': 1, 'y': 2})


# 如果想将一个函数的参数格式转接到其内部的一个函数
def bar(x, y, z):
    print(x, y, z)


def wrapper(*args, **kwargs):
    bar(*args, **kwargs)


wrapper(1, 2, 3)


# 命名关键字参数
def foo(x, y, *args, m, n, **kwargs):
    print(x, y)
    print(args)
    print(m, n)
    print(kwargs)


foo(1, 2, 3, 4, m=3, n=4, a=1, b=2)  # m,n只能用这种方法进行赋值

# 返回值
l = [1, 2, 3, 4]
n = l.pop()  # n就为pop（）的返回值
print(l)
print(n)


# return返回函数运行后的结果
# 是一个函数结束的标志，一个函数可以有多个return，默认return None
# return的返回无类型和个数的限制
def factory(a):
    print('正在制造手机')
    return a


factory(1)
print(factory(1))


def factory1(a):
    if a == 1:
        return 3
    return 2, 5, True


print(factory1(1))
print(factory1(0))


# 利用函数结束循环
def factory(a):
    print('===')
    while True:
        while True:
            if a == 3:
                return
            print(a)
            a += 1


factory(1)

# 函数局部变量和全局变量
# 外部不能访问内部的变量
# 函数内部可以访问外部的变量
# 函数里面不能修改外部变量
x = 123


def fun():
    print(x)


fun()


# global如果修改外部变量需要变成全局变量
def fun():
    global x
    x = x + 1
    print(x)


fun()


# nonlocal修改嵌套函数之外的
def fun2():
    b = 100

    def fun3():
        nonlocal b
        b += 1
        print(b)

    fun3()


fun2()

# 常用的内置函数
# str(),int(),etc.
# 绝对值
print(abs(-5))
# all(可迭代对象）返回bool值，要求里面均为真
print(all([1, '', None]))
print(all([1, 3, 4]))
print(all([]))
print(all(''))

# any(可迭代对象），返回bool值，要求里面一个为真
print(any([1, 2, '']))

# reverse,sorted正序反序

# 最大值,最小值

l = [1, 2, 3, 6, 4, 8]
print(max(l))
print(min(l))

# 求和
print(sum(l))

# ascii编码
# ord 字符转化成编码
print(ord('你'))
# chr 编码转化成字符
print(chr(20320))

# 拉链函数 zip
# 多出来的元素会被抛弃
t1 = ['a', 'b', 'c', 'd']
t2 = [1, 2, 3]
print(zip(t1, t2))
print(dict(zip(t1, t2)))

# exec 执行字符串里的代码
exec('print(1)')
exec(
    'for i in range(10):'
    'print(i)'
)

# 匿名函数；没有名字的函数
# 用于仅仅临时使用一次，没有重复使用的需求
print(lambda x, y: x + y)
print((lambda x, y: x + y)(1, 2))
f = lambda x, y: x + y
print(f(1, 2))
# max,min,sorted连用
salaries = {
    'xialuo': 300000,
    'xishi': 400,
    'dahai': 3000
}
# max默认只能比较key
print(max(salaries))


# 求工资最大值的人名
# 有名函数
def func(name):
    return salaries[name]


print(max(salaries, key=func))
# 匿名函数
print(max(salaries, key=lambda name: salaries[name]))

# 排序
print(sorted(salaries, key=lambda name: salaries[name]))


# 递归函数
# 自己调用自己，调用函数的过程直接或者间接调用此函数

# 直接调用
def foo(n):
    print('foo')
    if n == 1:
        return
    foo(n + 1)


foo(0)


def age(n):
    if n > 1:
        return age(n - 1) + 2
    elif n == 1:
        return 18


print(age(5))

L = [1, [2, [3, [4, [5, [6, [7]]]]]]]


def search(L):
    for n in L:
        if type(n) is not list:
            print(n)
        else:
            search(n)


search(L)


# 闭包函数
# 闭包是该函数是一个内部函数，内部函数名字再外部被引用
def outer():
    print('外面的函数')

    def inner():
        print('里面的函数')

    return inner  # 返回inner函数的内存地址


# outer()  # inner在这里被定义
inner = outer()
inner()


def outer(x, y):
    def func():
        print(x + y)

    return func


func = outer(1, 2)
func()
