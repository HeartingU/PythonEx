"""
文件操作
"""
# 绝对路径
f = open(r'D:\研究生\pythonEx\test-read', encoding='utf-8')
# print(f.read())
f.close()
# 相对路径
f = open(r'test-read', encoding='utf-8')
# print(f.read())
# 上下文管理:可以打开+关闭一个整体进行执行
with open(r'test-read', encoding='utf=8') as f:  # as就是赋值
    print(f.read())

# 打开方式，只读(r)，只写(w)，只追加写(a)
with open(r'test-read', mode='r', encoding='utf-8') as f:
    res1 = f.read()
    print('1111>>>', res1)  # 一次性读完
    res2 = f.read()
    print('2222>>>', res2)
    print(f.readable())
    print(f.writable())

# 只读模式
with open(r'test-read', mode='r', encoding='utf-8') as f:
    print(f.readline())
    print(f.readline())

with open(r'test-read', mode='r', encoding='utf-8') as f:
    for line in f:
        print(line)

with open(r'test-read', mode='r', encoding='utf-8') as f:
    L = []
    for line in f:
        L.append(line)
    print(L)

# 只写模式
# 当写文件的时候首先会清空内容，因为指针会跑到文件开头
with open(r'test-write', mode='w', encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    f.write('666')
    f.write('777\n')
    f.write('888')
    f.write('999\n0000')
# 把列表内容一行行写入
with open(r'test-write', mode='w', encoding='utf-8') as f:
    info = ['dahai', 'xialuo', 'xixi']
    for line in info:
        f.write(line + '\n')
# 不分行
with open(r'test-write', mode='w', encoding='utf-8') as f:
    f.writelines(info)

# 追加写模式,不能读只能写
# 当文件不存在时，会新建空文档，指针会在文件的末尾
with open(r'test-a', mode='a', encoding='utf-8') as f:
    print(f.readable())
    f.write('1111111\n')
with open(r'test-a', mode='a', encoding='utf-8') as f:
    f.write('2222222222\n')

# 二进制模式，一定不能指定encoding参数,可以操作文本(需要解码），视频，图片
with open('test.jpg', mode='rb') as f:
    data = f.read()
    print(data)
    print(type(data))

with open('test-wb.jpg', mode='wb') as f:
    f.write(data)

# decode 二进制解码成字符
# encode 字符编码成二进制
# 读的时候要解码
with open('test-b', mode='rb') as f:
    data = f.read()
    print(data)
    print(type(data))
    print(data.decode('utf-8'))
# 编码 写的时候转化成二进制写入
with open('test-wb', mode='wb') as f:
    f.write('dahai'.encode('utf-8'))
with open('test-wb', mode='rb') as f:
    data = f.read()
    print(data.decode('utf-8'))

# 可读可写模式
# r+t,不会创建新文件,会在末尾写
with open('test-rt', mode='r+t', encoding='utf-8')as f:
    print(f.readable())
    print(f.writable())
    msg = f.readline()
    print(msg)
    f.write('\n2222')
# w+t,会创建新文件,会清空并在开头写
with open('test-wt', mode='w+t', encoding='utf-8')as f:
    print(f.readable())
    print(f.writable())
    f.write('aaaaaaa\n')
    f.write('bbbbbb\n')

with open('test-wt', mode='w+t', encoding='utf-8')as f:
    f.write('11\n')
    f.write('22\n')
    # 移动字节数seek(移动的字节数，从头开始）,但是写还是会在末尾写
    f.seek(0, 0)
    msg = f.readline()
    print(msg)
# a+t
with open('test-at', mode='a+t', encoding='utf-8')as f:
    f.write('aaaaaaa\n')
    f.write('bbbbbb\n')
with open('test-at', mode='a+t', encoding='utf-8')as f:
    f.write('111\n')
    f.write('222\n')

# 指针移动
# seek()只有在t模式下的read（n），n代表字符的个数
# seek(offset,whence)
# offset:移动的字节数
# whence：0：参照文件开头，可以在t和b下使用
# 1：参照当前位置，必须在b模式下使用
# 2：参照末尾位置，必须在b模式下用
# b模式文件内指针的移动都是以字节为单位
# 一个汉字有三个字节，有些是四个
with open('seek', mode='rt', encoding='utf-8') as f:
    print(f.read(1))
    print(f.read(1))
    print(f.read(1))

with open('seek', mode='rb') as f:
    # 汉字读三个字节，字母读一个
    print(f.read(3).decode('utf-8'))
    print(f.read(1).decode('utf-8'))

with open('seek-ex', mode='rt', encoding='utf-8')as f:
    f.seek(3, 0)
    print(f.read(3))  # 读的是字符

with open('seek-ex', mode='rb')as f:
    f.seek(6, 0)
    print(f.read(3).decode('utf-8'))  # 读的是字节

with open('seek-ex', mode='rb')as f:
    msg = f.read(3)
    print(f.tell())  # 查看光标所在的字节数
    f.seek(3, 1)
    print(f.read(3).decode('utf-8'))

with open('seek-ex', mode='rb')as f:
    f.seek(0, 2)
    print(f.tell())
    f.seek(-3, 2)
    print(f.read(3).decode('utf-8'))

# 修改文件方式一：在内存修改
with open('change-doc', mode='rt', encoding='utf-8')as f:
    all_data = f.read()

with open('change-doc', mode='wt', encoding='utf-8')as f1:
    f1.write(all_data.replace('123', '789'))

# 修改文件方式二：读的方式打开源文件。写一个临时文件，读取完毕后删掉源文件
import os

with open('change-doc2', mode='rt', encoding='utf-8') as read_f, open('tmp', mode='wt', encoding='utf-8') as write_f:
    for line in read_f:
        write_f.write(line.replace('aaaaa', 'bbbbb'))
os.remove('change-doc2')
os.rename('tmp', 'change-doc2')

# 如何避免乱码
    # 字符的解码和编码方式要相同
# 日语
with open('badcode', 'w', encoding='shift_jis') as f1:
    f1.write('こんにちは')
with open('badcode', 'r', encoding='shift_jis') as f1:
    msg = f1.read()
    print(msg)
# 解码编码不同导致乱码或报错
with open('badcode', 'r', encoding='gbk') as f1:
    msg = f1.read()
    print(msg)
