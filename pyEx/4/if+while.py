# 登陆取款程序
# 理解while嵌套
user = 'dahai'
pwd = 123
balance = 5000
tag = True
while True:
    while tag:
        user1 = input('输入用户名')
        if user1 != user:
            print('你输入的用户名错误，请重试')
            continue
        pwd1 = int(input('输入密码'))
        if pwd1 == pwd:
            print('登陆成功')
            break
        else:
            print('密码输入错误，请重试')
    tag = False
    money = int(input('输入你的取款金额'))
    if balance > money:
        balance -= money
        print('取款%s成功，余额为%s' % (money, balance))
        break
    else:
        print('余额不足')
