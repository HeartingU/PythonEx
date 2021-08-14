'''
字符串操作
'''

res = 'dahai'
print(type(res))
# 按索引取值，只能取,字符串不能修改里面的字符
msg = "hello world"
print(msg[0])
print(msg[-1])
print(msg[0:5])  # 终止值是取不到的,默认步长是1
print(msg[0:5:2])
print(msg[5:0:-1])  # 步长为负会输出值倒过来
print(len(msg))  # 长度
# 成员运算in和not in：判断一个字符串是否存在于大字符串中
print('dahai' in 'dahai is ocean')
print('xiaohai' not in 'dahai is ocean')
# join操作
str1 = '真正的勇士'
str2 = '敢于直面惨淡的人生'
str3 = '敢于正视淋漓的鲜血'
print(','.join([str1, str2, str3]))

# 删除
name1 = 'dahai'
del name1

# 改动
# 全部变大(小）写upper,lower,需要赋值到新的字符串，原值是不会改变的
msg1 = 'abc'
msg2 = msg1.upper()
print(msg2)
print(msg1)
# 把第一个字母变成大写
letter = 'abcd'
print(letter.capitalize())
# 每个单词的首字母大写
letter_msg = 'hello world'
print(letter_msg.title())
# 把字符串切分成列表，默认空格字符切分
msgg = 'hello world python'
msgg1 = msgg.split()
msgg2 = msgg.split('l')
print(msgg1)
print(msgg2)
# 去掉字符串两边的字符，默认两边为空格字符
user = '         dahai       '
print(user.strip())

# 查询
# 查找子字符串在大字符串中的位置（返回起始索引）
# 默认范围是所有字符
msg = 'hello dahai is ocean'
print(msg.find('dahai'))
print(msg.find('dahai', 0, 4))

print(msg.index('dahai'))
# print(msg.index('dahai', 0, 4))
msg1 = 'dahai和dahai'
print(msg1.find('dahai'))
print(msg1.rfind('dahai'))
# 统计出现的次数
print(msg1.count('dahai'))
# 判断一个字符串中的数据是否是数字
num = '1818'
print(num.isdigit())
# 判断字母
letter1 = 'abc'
print(letter1.isalpha())
# 比较开头（结尾）的元素是否相同
msg1 = 'dahai is ocean'
print(msg1.startswith('dahai'))
print(msg1.endswith('ocean'))
print(msg1.endswith('an'))
# 判断是否全部为大写（小写）
print(msg1.isupper())
print(msg1.islower())

# 转义 \n 换行   \t 进格
print('hello \n world')
print('hello \t world')
print(r'\n')
