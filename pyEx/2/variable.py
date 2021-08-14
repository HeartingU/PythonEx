"""
变量：能够记录特征，让计算机存取。
定义变量:
变量名：相当于门牌号，是访问的唯一方式
赋值：=
值：状态
变量的命名规则：
   见名知意；
   变量名首字符不能是数字；
   变量名只能是字母数字和下划线的组合
变量的特性：
    变量是有id的（用id（）查询）。id是在内存中的位置
    类型（用type（）查询）
"""

name = "大海"
print(name)
name = "小孩"
print(name)
# 复杂变量名的命名
# 下划线法
age_of_dahai = 18
# 驼峰体
AgeOfDahai = 18

# 常量（全部大写）：不变的量 告诉别人不能改
NAME = '小海'

'''
字符串类型：str
作用：记录描述性质的数据
定义： 在引号内按照从左到右的顺序依次包含一个个字符，引号可以是单双三引号
'''

name0 = 'dahai'
name1 = "dahai"
name2 = '''dahai'''
# 字符串中如果要有引号
print("my name is 'dahai'")
print('my name is "dahai"')
# 字符串相加
print('dahai' + 'ocean')
# 字符串乘法
print('dahai' * 10)

'''
用户交互
    输入数据后，程序执行完毕后反馈信息
'''
# print交互
print(1)
# 输入输出I/O
name = input("请输入名字")
print(name)

'''
字符串格式化输出：使用占位符 ex. %s %d
%s 可以接受所有的数据类型
%d 只能接受数字
'''

name = 'dahai'
age = 18
print('my name is %s, and my age is %s', name, age)
name = input('请输入名字')
print('my name is %s, and my age is %s' % (name, age))  # 一个值的时候就没必要把变量放在括号里了
print('my name is %s, and my age is %s' % (name, 18))

'''
数字类型
'''
# 整形int
age = 19
print(type(age))
# 浮点型float
weight = 150.5
print(type(weight))
# 运算符：
#   算术运算
#       加+
#       减-
#       乘*
#       除/ 结果是float
#       地板除// 结果是向下取整
#       取余%
#       乘方**

# 比较运算符 结果都为bool值（True或者False）
#   等于 ==
#   不等于 ！=
#   大于>
#   小于<
#   大于等于>=
#   小于等于>=

'''
bool类型
用于判断条件
True or False
'''
tag = True
print(type(tag))

'''
复数类型complex
线性参数
'''
x = 1 - 2j
print(type(x))

'''
列表list
记录多个任意类型的值
'''
L = [1, 2, 3, 'ggg', [2, 3, 4, 5]]
print(type(L))
# 取第一个值用索引
print(L[0])
print(L[-1])
print(L[0:2])
'''
字典dic
记录的是key：value一对值
'''
info = {'name': 'xiaohai', 'age': 18}
print(info['name'])
print(info['age'])
'''
元组tuple
记录多个值，并没有改动的需求,元组的值不能变动，但是元组中的列表中的元素可以变动
取值和列表一样
'''
t = (1, 2, 'dahai', (2, 3), [2, 3])
print(type(t))
print(t[0])
'''
集合set
用于关系运算（交并补）
元素不能重复
集合中的元素是无序的
'''
s = {1, 2, 3, 4, 5, 'dahai'}
print(type(s))
s1 = {'a', 'b', 'c'}
s2 = {'a', 'c', 'd'}
print(s1 & s2)  # 求交集
print(s1 | s2)  # 求并集
print(s1 - s2)  # 求补集
