#字符串的驻留机制 同一判定 值相等判定

a = "hello"
b = "hello"
print(id(a),id(b)) #-相同的字符串只会在内存中存储一份
print(a is b)
print(a == b)
c='sasdekjknhuyuwiue'
d = 'sa'
print(d in c,"sddds")

# 字符串 常用的查找方法
# find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束）范围，则检查是否包含在指定范围内，
a='这里是是一段测试的文本'
len(a) #返回字符串长度
b= a.startswith('这里') #检查字符串是否以指定的字符串开头
c=a.endswith('文本') #检查字符串是否以指定的字符串结尾
d=a.find('是') #检查字符串中是否包含子字符串
e=a.rfind('是') #从右边开始查找
f=a.count('是') #返回子字符串在字符串中出现的次数
g=a.isalnum() #检测字符串是否由字母和数字组成

#去除首尾信息
a='  asd  '
b=a.strip() #去除首尾空格
c=a.lstrip() #去除左边空格
d=a.rstrip() #去除右边空格
e = '* asd  *'
f=e.strip('*') #去除首尾指定字符

# 大小写转换
a='ASD'
b=a.lower() #转换为小写
c=a.upper() #转换为大写
d=a.swapcase() #大小写互换
e=a.capitalize() #首字母大写
f=a.title() #每个单词首字母大写

# 格式排版
a='hello'
b=a.center(10) #居中
c=a.ljust(10) #左对齐
d=a.rjust(10) #右对齐

# 特征判断方法
a='123'
b=a.isdigit() #判断是否为数字
c=a.isalpha() #判断是否为字母
d=a.islower() #判断是否为小写
e=a.isupper() #判断是否为大写
f=a.isspace() #判断是否为空格
g=a.istitle() #判断是否为首字母大写
h =a.isalnum() #判断是否为字母和数字


# 字符串format 格式化 _ 数字格式化
# format() 方法用于格式化字符串
a = "我叫{},今年{}岁,{}是个best man"
b = a.format("cdx",18,"cdx") #{} 为占位符
print(b)
c = '我叫{0},今年{1},我是{0}的粉丝'.format('cdx',18)
c.format('cdx',18)

e = '我叫{name},今年{age},我是{name}的粉丝'
f = e.format(name='cdx',age=18) #通过关键字参数传入

# 填充与对齐
# g='我叫{name:^*8},今年{age},我是{name}的粉丝'
# h=g.format(age=18) #填充与对齐
# print(h)


#可变字符串
import io

s = "abcdefghijklmn"
sio = io.StringIO(s) #创建一个可变字符串
print(sio)
print(sio.getvalue()) #获取字符串
sio.seek(3) #移动指针到第三个位置
sio.write("***") #写入
print(sio.getvalue())  #获取字符串

# 类型转化的总结
# int('123') #字符串转整数
# # long('123') #字符串转长整数
# float('123.456') #字符串转浮点数
# complex('1+2j') #字符串转复数