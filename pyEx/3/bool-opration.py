"""
bool类型
True or False
数据均带有bool值, none , 0, null均返回False
"""

tag = True
print(type(tag))

tag1 = ''
# tag1 = 0
# tag1 = 2
# tag1 = []
# tag1 = {}
if tag1:
    print('数据类型自带True')
else:
    print("数据类型自带False")
