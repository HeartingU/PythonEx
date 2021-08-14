"""
for循环
"""
# 遍历列表
list_names = ['dahai', 'xiaohai', 'xishi']
for n in list_names:
    print(n)
# 遍历字典，默认是遍历key值
names = {'name1': 'dahai', 'name2': 'xiaohai', 'name3': 'xishi'}
for i in names:
    print(i)

for i in names.keys():
    print(i)
# 遍历value
for i in names:
    print(names[i])

for i in names.values():
    print(i)
# 遍历键值对
for i in names.items():
    print(i)

# range(起始索引，结束索引，步长)
a = range(0, 5, 2)
print(type(a))
# range迭代器可以节省内存空间
print(list(a))

for i in range(0, 5):
    print(i)

for i in [0, 1, 2, 3, 4]:
    print(i)

for i in range(0, len(list_names)):
    print(list_names[i])

# 和break和continue连用
names = ['dahai', 'xialuo', 'xishi']
for i in names:
    if i == 'xialuo':
        continue
    print(i)
for i in names:
    if i == 'xialuo':
        break
    print(i)
# for + else:
# else只会在没有break结束的时候在最后进行运行
for i in range(10):
    print(i)
else:
    print('==========')
for i in range(10):
    if i == 4:
        break
    print(i)
else:
    print('==========')
#for 嵌套
# 打印9*9乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}='+ str(i*j), end=' ')
    print()
# 打印9*9乘法口诀表(倒过来)
for i in range(9,0,-1):
    for j in range(9,9-i,-1):
        print(f'{i}*{10-j}=' + str(i * (10-j)), end=' ')
    print()