"""
元组：tuple
元组不能通过索引修改
元组中的列表中的值可以更改
"""
t = (1, 2, 'dahai', (2, 3), [2, 3])
print(t)
print(type(t))
print(t[0])
# 元组中的列表中的值可以更改
t[4][0] = 8
print(t)
#想修改可以改成列表
t1 = list(t)
t1[0] = 8
print(t1)
t = tuple(t1)
print(t)
#别的方法和列表一样