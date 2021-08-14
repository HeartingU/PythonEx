"""
集合：set
集合中每个值都是不可变类型，所以一般只是用来关系运算
"""

s = {1, 2, 3, 4, 5, 'dahai'}
# 增加
s.add('xiaohai')
print(s)
s.add(1)
print(s)
# 删除
res = s.pop()
print(s)
print(res)
# 指定删除
s.remove('dahai')
print(s)
# 改
s.update(['lanhai', 'zihai'])
print(s)
# 集合去重
names = ['dahai', 'xiaohao', 'xialuo', 'xishi', 'dahai', 'dahai']
s = set(names)
print(s)
s1 = list(s)
print(s1)
