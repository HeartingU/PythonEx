"""
对象
    可以用类生成
"""

# 调用类就是类的实例的初始化
# 类的返回值称之为类的一个对象、实例
import function


class Teacher:
    # 相同的特征、属性
    name = 'dahai'
    age = 18
    gender = 'male'

    # 技能
    # 函数、方法
    def course(self):
        # self是一个位置形参
        print('course')

    # 测试
    print('类的定义')


t1 = Teacher()
t2 = Teacher()
t3 = Teacher()
print(t1)
# 对象的方法
print(t1.course)

print(Teacher.__dict__)
# 对象没有独立的属性
print(t1.__dict__)
t1.course()
Teacher.course(11)
# 对象属性的修改
t1.name = 'xialuo'
print(t1.name)
# 对象独立创造了属性
print(t1.__dict__)
del t1.name
print(t1.name)


# 生成对象之__init__()
class Teacher:
    # 相同的特征、属性
    xxx = '我是一个属性'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 技能
    # 函数、方法
    def course(self, name):
        # self是一个位置形参
        print('course' % name)

    # 测试
    print('类的定义')


dahai = Teacher('dahai', 18, 'male')
xialuo = Teacher('xialuo', 22, 'female')

print(dahai.name)
print(xialuo.age)

dahai.name = 'xiaohai'
print(dahai.name)
# dahai.course('dahai')

dahai = Teacher('dahai', 18, 'male')
xialuo = Teacher('xialuo', 22, 'male')
guan = Teacher('guan', 23, 'male')
# 对象属性查找
dahai.xxx = '我是属性'
print(dahai.xxx)


# 类中方法和属性是类中所有对象共享的

# 绑定方法和非绑定方法
class A:
    def f(self):
        print(self)
        print('我是self的方法')


# self就是传入的那个对象,调用方法的时候会自动把对象传入，一般方法得到参数用self表示（self不占用其他方法的参数位置）
a = A()
a.f()
print(a)
# 类的调用必须传入对象
A.f(a)


# class B:
#
#     def f(self):
#         print(self)
#         print('我是绑定类的方法')
#
# B.f()

class B:
    @classmethod
    def f(self):
        print(self)
        print('我是绑定类的方法')


B.f()


# 非绑定方法\静态方法

class C:
    # 不会自动传入参数
    @staticmethod
    def f():
        print('我是非绑定方法')


C.f()
