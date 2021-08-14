"""
python 技巧
"""

'''
变量的交换
'''
a = 1
b = 2
# 常用做法
tmp = a
a = b
b = tmp
# 简洁做法
a, b = b, a

'''
字符串格式化
'''
name = "Ross"
country = "China"
age = 28
# 常见做法
print("Hi, I'm" + name + ". I'm from " + country + ". And I'm " + str(age) + ".")
# 简洁做法1(%+类型首字母)
print("Hi, I'm %s. I'm from %s. And I'm %d." % (name, country, age))
# 简洁做法2(format())
print("Hi, I'm {}. I'm from {}. And I'm {}.".format(name, country, age))
# 简洁做法3(format())用花括号带索引获取内容
print("Hi, I'm {0}. Yes, I'm {0}.".format(name))
# 简洁做法4(f{表达式})
print(f"Hi, I'm {name}. I'm from {country}. And I'm {age + 1}.")

'''
yield 语法
每当计算出一个元素就马上送出去，与return的区别是不会结束函数，函数会继续执行
'''


# 常见做法
def fibnacci(n):
    a = 0
    b = 1
    nums = []
    for _ in range(n):
        nums.append(a)
        a, b = b, a + b
    return nums


# 简洁做法
def fibnacci1(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for i in fibnacci(10):
    print(i)

'''
列表解析式
'''
fruit = ["apple", "pear", "pineapple", "orange", "banana"]
# 改成大写
# 常见做法
for i in range(len(fruit)):
    fruit[i] = fruit[i].upper()
# 简洁做法
fruit = [x.upper() for x in fruit]
# 筛选以a为开头的水果
# 常见方法
filtered_fruit = []
for f in fruit:
    if f.startswith("a"):
        filtered_fruit.append(f)
# 简洁做法
filtered_fruit = [x for x in fruit if x.startswith('a')]

'''
循环技巧
enumerate函数
'''
# 得到索引值和内容
for i, x in enumerate(fruit):
    print(i, x)

'''
反向遍历
'''
for i, x in enumerate(reversed(fruit)):
    print(i, x)

'''
顺序遍历（a~z）
'''
for i, x in enumerate(sorted(fruit)):
    print(i, x)

'''
字典的合并操作
'''
a = {"ross": "123456", "xiaoming": "abc123"}
b = {"lilei": "111111", "zhangsan": "121345678"}

# 常见做法
c = {}
for k in a:
    c[k] = a[k]
for k in b:
    c[k] = b[k]

# 简洁做法,解包做法
c = {**a, **b}

'''
三元运算符
'''
score = 90
# 常见做法
if score > 60:
    s = "pass"
else:
    s = "fail"
# 简洁做法
s = "pass" if score > 60 else "fail"

'''
序列解包
'''
name = "San Zhang"
# 常见做法
str_list = name.split()
first_name = str_list[0]
last_name = str_list[1]
# 简洁做法
first_name, last_name = name.split()

'''
with语句
'''
# 常见打开文件方式
f = open("1.txt", "r")
s = f.read()
f.close()
# 防止忘写close以至于占资源的方式
with open("1.txt", "r") as f:
    s = f.read()
