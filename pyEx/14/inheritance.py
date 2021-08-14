'''
继承，派生
    子类可以遗传或者重用父类的属性或者方法
    可以减少代码冗余

'''


class Parent():
    xxx = 123

    def run(self):
        print("我是父类")


class Sub(Parent):
    xxx = 222


obj = Sub()
# obj.xxx  = 111
print(obj.xxx)
obj.run()


# 继承解决代码冗余问题
class People:
    school = 'turing'


class Student():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def play(self):
        print('%s play football' % self.name)


class Teacher():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def course(self):
        print('%s course' % self.name)


s1 = Student('zhouyang', 38, '男')
print(s1.__init__)
t1 = Teacher('ouou', 23, '女')
print(t1.__init__)


class People:
    school = 'turing'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(People):

    def play(self):
        print('%s play football' % self.name)


class Teacher(People):

    def course(self):
        print('%s course' % self.name)


s1 = Student('zhouyang', 38, '男')
print(s1.__dict__)
t1 = Teacher('ouou', 23, '女')
print(t1.__dict__)


# 如果子类有新的属性需求？
class Student(People):
    def __init__(self, name, age, sex, score=0):
        # 相当于调用父类方法
        People.__init__(self, name, age, sex)
        self.score = score

    def play(self):
        print('%s play football' % self.name)


s2 = Student('zhouyang', 38, '男', 99)
print(s2.__dict__)


# 单继承的属性查找
# 优先级为对象，对象的类，对象的父类
class Foo():
    xxx = 444
    pass


class Bar1(Foo):
    xxx = 333
    pass


class Bar2(Bar1):
    xxx = 222


obj = Bar2()
print(obj.xxx)


class Foo:
    def f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')


class Bar(Foo):
    def f1(self):
        print('Bar.f1')


obj = Bar()
obj.f2()
obj.f1()


# 多继承,查找方式为广度优先查找
class G:
    x = 'G'
    pass


class E(G):
    x = 'E'
    pass


class F(G):
    x = 'F'
    pass


class B(E):
    x = 'B'
    pass


class C(F):
    x = 'C'
    pass


class D(G):
    x = G
    pass


class A(B, C, D):
    x = 'A'
    pass


obj = A()
# obj.x = 11
print(obj.x)

print(A.mro())  # 查找顺序


# 派生类重用父类方法


class Student(People):
    def __init__(self, name, age, sex, score=0):
        # 相当于调用父类方法
        # People.__init__(self, name, age, sex)
        #super(Student, self).__init__(name, age, sex)
        super().__init__(name, age, sex)
        self.score = score

    def play(self):
        print('%s play football' % self.name)


class Teacher(People):

    def course(self):
        print('%s course' % self.name)
