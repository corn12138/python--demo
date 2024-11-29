#10a = 0
#if = 9
# from unittest import FunctionTestCase #引入关于单元测试的模块

_student_s = 2
print(_student_s)


# 变量的引用和垃圾回收机制
a = 1
print(a)
del a;
# print(a,"sc")


#常量_链式赋值_系列解包赋值
MAX_AGE = 100  #常量  --  常量的命名规则是所有字母大写，单词之间用下划线连接--PYTHON中没有真正的常量
a = b = c = 1 #链式赋值
print(a,b,c,"<链式复制")
a,b,c = 10,20,30 #系列解包赋值
print(a,b,c,"<系列解包赋值")

c,d =9,10
c,d = d,c #交换两个变量的值
print(c,d,"<交换两个变量的值")

#最基本的内置数据类型
a = 123 #整数
b = 123.456 #浮点数
c = "hello world" #字符串
d = True #布尔值
e = None #空值
# print(type(a),type(b),type(c),type(d),type(e))
print(type(b))

# 数字和基本运算
a = 10/6 #浮点数除法
b = 10//6 #整数除法
c= 10%6 #取余
d=10**6 #幂运算
v= divmod(10,6) #返回商和余数
print(a,b,c,d,v)

#整数_不同进制_其他类型转换成整数
a = 10
b = 0b10 #二进制
c = 0o17 #八进制
d = 0x10 #十六进制
print(int(10.6),int("10"),int("10",16),'其他类型转换成整数') #其他类型转换成整数
print(a,b,c,d,'不同进制')
print(int(a),int(b),int(c),int(d),'其他类型转换成整数') #其他类型转换成整数

f = 10**100 #大整数
print(f,'google')

#浮点数_自动转换_强制转换_增强赋值运算符

a = 3.14
b = 314e-2
c=float("2.5")
x=y=9
# y/=x+2
y*=x+4
v=round(3.1415926) #四舍五入
print(a,b,c,y,v,'浮点数')

#时间的表示_unix时间点_毫秒微秒_time模块

