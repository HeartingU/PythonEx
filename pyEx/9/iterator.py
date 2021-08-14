'''
迭代器
'''

# 可迭代对象,自带_iter_方法
# 字符串，列表，字典等容器都是可迭代对象
# 文件属于迭代器
g = [1, 2]
print(g.__iter__())
# g.__iter__()会生成迭代器
dic = {'x': 1, 'y': 2, 'z': 3}
# 迭代器
iter_dic = dic.__iter__()
# 取值类似for循环遍历
print(iter_dic.__next__())
print(iter_dic.__next__())
print(iter_dic.__next__())
# 在取值的话就会报错，因为值已经取完了

# 列表不依赖索引取值
L = [1, 2, 3]
iter_L = L.__iter__()
print(iter_L.__next__())
print(iter_L.__next__())
print(iter_L.__next__())

# 误区
l = [1, 2, 3]
print(l.__iter__().__next__())
print(l.__iter__().__next__())

dic = {'x': 1, 'y': 2, 'z': 3}
# 和iter_dic = dic.__iter__()等价
iter_dic = iter(dic)
# 和iter_dic.__next__()等价
next(iter_dic)

# 解决迭代器报错（取完值之后报错）
# 异常捕获
while True:
    try:
        print(next(iter_dic))
    except StopIteration:
        break

print('================')
while True:
    try:
        print(next(iter_dic))
    except StopIteration:
        break

# for循环，迭代器循环
dic = {'x': 1, 'y': 2, 'z': 3}
for k in dic:
    print(k)
for k in dic:
    print(k)
