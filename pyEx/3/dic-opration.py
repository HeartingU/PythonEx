"""
dict：字典
key必须是是不可变类型则无法提取
"""
info = {'name': 'xiaohai', 'age': 18}
info1 = {(1, 2, 3): 'name'}
print(info1[(1, 2, 3)])
# 生成字典方式
dic = dict(x=1, y=2)
print(dic)
# 增加
info['addr'] = 'beijing'
print(info)
# 键值对个数
print(len(info))
# 成员运算，针对key
print('name' in info)
print('dahai' in info)
# 删除
info1.clear()
print(info1)
del info['addr']
print(info)
# 删除不存在的键值对会报错
# del info['gender']
# print(info)
res = info.pop('name')
print(info)
print(res)
# popitem把最后一对键值对删除，返回的是一个元组
res1 = info.popitem()
print(info)
print(res1)

info = {'name': 'honghai', 'age': 18, 'addr': 'changsha'}
# 改
print(info)
info.update({'name': 'xiaohai'})
print(info)
# setdefault:有则不动返回原值，无则添加返回新值
res1 = info.setdefault('name', 'xxxx')
print(info)
print(res1)
res1 = info.setdefault('gender', 'male')
print(info)
print(res1)
# 查,查不存在的key会报错,或者用get
print(info['name'])
print(info.get('name'))
print(info.get('xxxx'))
#取出所有的key
res1 = info.keys()
print(res1)
print(type(res1))
print(list(res1))
print(type(list(res1)))
#取出所有的value
res2 = info.values()
print(res2)
print(type(res2))
print(list(res2))
#取出所有的键值对
res3 = info.items()
print(res3)
print(list(res3))