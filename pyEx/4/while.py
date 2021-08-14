"""
while循环
"""

# 死循环
# while True:
#    print('1111')
#    print('22222')
db_user = 'dahai'
db_pwd = '123'
# while True:
#     input_user = input('请输入用户名')
#     input_pwd = input('请输入密码')
#     if input_user == db_user and input_pwd == db_pwd:
#         print('登陆成功')
# # break:跳出本层循环
#         break
#     else:
#         print('登陆失败')
# while + 条件范围
count = 1
while count <= 10:
    print(count)
    count += 1
# continue:结束本次循环
# continue不要放在循环体的最后一行，否则没有意义
start = 0
while start < 8:
    start += 1
    if start == 4:
        continue
    print(start)
# while + else
# else只会在没有break结束的时候在最后进行运行
n = 0
while n < 6:
    n += 1
    if n == 6:
        break
    print(n)
else:
    print('==========')
print('--------------')

#while 遍历列表
names = {'dahai', 'xiaohai', 'xishi'}
i = 0
while i < len(names):
    print(names[i])
    i += 1