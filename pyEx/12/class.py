"""
类(自定义变量）
    属性
    技能
"""


# 类名的首字母大写
class Person:
    pass


# 先定义类
class Teacher:
    # 相同的特征、属性
    name = 'dahai'
    age = 18
    gender = 'male'

    # 技能
    # 函数、方法
    def course(self):
        #self是一个位置形参
        print('course')

    # 测试
    print('类的定义')

#调用类的属性
print(Teacher.__dict__)
print(Teacher.name)

#类的方法调用
print(Teacher.course)
Teacher.course(1)

# 修改类里面的属性值
Teacher.name='xialuo'
print(Teacher.name)
# 添加类的属性（类似于字典）
Teacher.play = 'basketball'
print(Teacher.__dict__)
# 删除属性
del Teacher.play
print(Teacher.__dict__)

