"""
if 判断
    if 条件：
        代码体
    else:
        代码体
"""
# tag = True
tag = 1 == 3
if tag:
    print('条件满足')
else:
    print('条件不满足')

'''
逻辑运算符： and or not
and：连接左右两个条件，只有两个条件都成立的情况下会返回true
or: 只要有一个条件成立则返回true
not: 返回相反的条件

not的优先级是最高的，就是把紧跟其后的那个条件去反， not与其后面的条件不可分割
如果语句既有and又有or，那么先用括号把and的左右两个条件括起来然后进行运算
'''

name = 'dahai'
num = 20
# and
print(18 < num < 26 and name == 'dahai')
print(num > 18 and 1 > 3)
# or
print(1 > 3 or num > 18)
# not
print(not 1 > 3)

# if加上逻辑判断
cls = 'human'
sex = 'female'
age = 18
if cls == 'human' and sex == 'female' and 16 < age < 22:
    print('开始表白')
else:
    print('表白失败')

# 三目运算(只能对if else)： 一行代码写if else
a = 6
print('满足条件') if a > 5 else print('不满足条件')

# elif,多分支：但凡有一个条件成立，就不会往下判断了
# if的优先级最高，其次是elif，最后是else
score = 80
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('普通')
else:
    print('很差')

# if嵌套:外面的if和里面的if要同时满足才能执行里面的if

if cls == 'human' and sex == 'female' and 16 < age < 22:
    print('开始表白')
    is_success = '我愿意'
    if is_success == '我愿意':
        print('在一起')
    else:
        print('我逗你玩呢')
else:
    print('表白失败')