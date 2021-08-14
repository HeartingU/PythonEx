"""
list列表
"""

L = ['dahai', 1, 1.2, [1, 'xiaohai']]
# 查询
print(L)
print(L[0])
print(L[-1])
print(L[3])
# 更改
L[0] = 'honghai'
print(L)
# 切片:顾头不顾尾
print(L[0:3])
print(L[0:3:2])
# 长度
print(len(L))
# 成员运算
print('honghai' in L)
print('honghai' not in L)
# 个数
print(L.count('honghai'))
# 位置：索引
print(L.index('honghai'))
# print(L.index('honghai',2,3))
# 增加:append在末尾增加元素
L.append('lanhai')
print(L)
# 插入：insert指定位置插入元素
L.insert(0, 'huanghai')
print(L)
# extend：插入多个元素在末尾
L.extend(['lvhai', 'zihai'])
print(L)
# 删除
del L[0]
print(L)
# 指定删除
L.remove('zihai')
print(L)
# 从列表中拿出一个值，pop
L.pop()
print(L)
res = L.pop(0)
print(res)
print(L)
# 清空列表
# L.clear()
# print(L)

# 反序：reverse
L.reverse()
print(L)
# 排序：sort,只对数字列表而言
l1 = [1, 3, 2, 6, 4, 98]
l1.sort(reverse=True)
l1.sort(reverse=False)
print(l1)
