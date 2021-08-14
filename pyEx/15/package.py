'''
封装
    将内容隐藏起来，对外不对内
    在类内定义的属性加__开头（定义封装）
    在外部无法进行封装
'''


class Foo:
    __x = 11
    y = 22

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print('func')

    def get_info(self):
        print()


# 在外面无法访问
# print(Foo.__x)
print(Foo.y)
print(Foo.__dict__)
print(Foo._Foo__x)  # 隐藏方式,语法上的变形


class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def tell_info(self):
        print('name:%s age:%s' % (self.__name, self.__age))

    def set_info(self, name, age):
        if type(name) is not str:
            print('名字必须为字符串')
            return
        if type(age) is not int:
            print('年龄必须为整形')
            return
        self.__name = name
        self.__age = age


obj = People('dahai', 18)
# 通过接口间接查看属性
obj.tell_info()
# 通过接口间接修改属性
obj.set_info('xialuo', 22)
obj.tell_info()


class ATM:
    # 把内部用户不需要知道的功能封装起来
    def __card(self):
        print('插卡')

    def __auth(self):
        print('用户认证')

    def __input(self):
        print('输入取款金额')

    def __print_bill(self):
        print('打印账单')

    def __take_money(self):
        print('取钱')

    # 在内部做一个接口一次调用
    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()


a = ATM()
a.withdraw()


# property把方法封装成属性
class People:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)


obj = People('dahai', 70, 1.8)
# 加property之前调用方式
# print(obj.bmi())
# 加property之后调用方式
print(obj.bmi)
