# 函数的基本概念_内存分析_函数分类_定义和调用
# 函数的定义和调用
def add(a,b,c):
    '''文档字符串--完成三个数的加法，并返回值'''
    sum = a + b + c
    print("{0} {1} {2}三个数的和是：{3}".format(a,b,c,sum))
    return sum

print(add) # 是一个函数对象
print(id(add)) # 函数的内存地址
print(type(add)) # 函数的类型
add(1,2,3)
add(10,20,30)

#形参和实参_文档字符串_函数的注释
#形参：定义函数时，小括号中的变量，本质是变量
#实参：调用函数时，传递给函数的数据，本质是值
def print_info(a,b):
    '''
    实现两个参数的比较，并返回较大的值
    :param a: 一个参数
    :param b: 一个参数
    :return:  返回较大的参数
    '''
    if a>b:
        print("{0}大于{1}".format(a,b))
        return a
    else:
        print("{0}小于{1}".format(a,b))
        return b
print(10,90)
print(10,5)

# help(print_info) # 查看函数的文档字符串
print(print_info.__doc__) # 查看函数的文档字符串

def print_star(n):
    '''
    打印n个星号
    :param n:
    :return:
    '''
    s = "*" * n
    return s

print(print_star(10))
print(print_star.__doc__)


#返回值详解
def my_avg(a,b):
    '''
    实现两个数的平均值，并返回
    :param a:
    :param b:
    :return:
    '''
    return (a+b)/2

a1 = my_avg(10,20) *120 +3
print(a1)

def printShape(n):
    '''
    打印n行的图形
    :param n:
    :return:
    '''
    s1 = "#" *n
    s2 = "$" *n
    return [s1,s2]

c = printShape(5)
print(type(c))
print(type(printShape(3)))
print(type(printShape))

# 函数也是对象_内存分析
def my_test(n):
    print("*"*n)

c = my_test # 函数也是对象--指向的还是同一个函数-内存地址相同
b = c # 函数也是对象
print(id(c))
c(2)
b(3)
# 上述代码就是 两个变量 指向的是--同一个函数对象
print(my_test,"函数对象")
print(id(my_test),"函数内存地址")
print(type(my_test),"函数类型")

zhengshu = int
print(zhengshu(3.14)) # 类型转换
s = str
print(s(3.14)) # 类型转换
# str ='ddd'
# print(str)
# print(str(3.14)) # 报错了--原因是str是一个字符串，不是一个函数


# 变量的作用域_全局变量_局部变量_栈帧内存分析讲解

# a =100
# def f1():
#     global a        #  声明为全局变量
#     a = 4
#     b = 3
#     print(a+b)
# f1()
# print(a)

# a = 100
# def f1(a,b,c):
#     print(a,b,c)
#
#     print(locals(),"查看局部变量") # 查看局部变量
#     print("$"*2000)
#     print(globals(),"查看全局变量") # 查看全局变量
#
# f1(1,2,3)

# 局部变量和全局变量_效率测试
import time
a = 100
def test01():
    start = time.time()
    global a
    for i in range(100000000):
        a += 1

    end = time.time()
    print("test01耗时：{0}".format(end-start))

def test02():
    start = time.time()
    c=1000
    for i in range(100000000):
        c += 1

    end = time.time()
    print("test02耗时：{0}".format(end-start))

test01()
test02()

#参数的传递_传递可变对象_内存分析
  #可变对象有：列表、字典、集合、自定义对象、函数对象、模块对象
  #不可变对象有：数字、字符串、元组、布尔值、None
b = [10,20]

def f2(m):
    print("m=",id(m))
    m.append(30)
f2(b)
print("b:",id(b))
print(b)
# 上述代码 --对于可变对象 传递的是引用，对于不可变对象 传递的是值
# 也就是说 m在append的时候 会改变b的值，因为m和b指向的是同一个对象


#参数的传递_传递不可变对象_内存分析
ac = 100
def fc1(n):
    print("n=",id(n))
    print("n=",id(n))
    print(n)
fc1(ac)
print("ac=",id(ac))

# 写 操作
def fc2(n2):
    print("n2=",id(n2))
    n2+=200 # 由于 n+=200 是一个写操作，所以会开辟新的内存空间 --所以两者不是同一个对象
    print("n2=",id(n2))
    print(n2)          
fc2(ac)
print("ac=",id(ac),ac)
print("*"*100)
print()
#浅拷贝和深拷贝_内存分析

import copy

def testCopy():
    '''
    浅拷贝
    :return:
    '''
    a = [10,20,[5,6]]
    b = copy.copy(a)
    print("a=",id(a),"浅拷贝",a)
    print("b=",id(b),"浅拷贝",b)
    b.append(30)
    b[2].append(7)
    print("浅拷贝后 修改b的值")
    print("a",a)
    print("b",b)


def testDeepCopy():
    '''
    深拷贝
    :return:
    '''
    a = [10,20,[5,6]]
    b = copy.deepcopy(a)
    print("a=",id(a),"深拷贝",a)
    print("b=",id(b),"深拷贝",b)
    b.append(30)
    b[2].append(7)
    print("深拷贝后 修改b的值")
    print("a",a)
    print("b",b)
testCopy()
print("*"*100)
testDeepCopy()

print("*"*100)
print()

#参数的传递_不可变对象含可变子对象_内存分析
#传递不可变对象时，不可变对象中包含可变对象，那么可变对象的值是可以改变的
a = (10,20,[5,6])
print("a=",id(a))
def f3(m):
    '''
    传递不可变对象时，不可变对象中包含可变对象，那么可变对象的值是可以改变的
    :param m:
    :return:
    '''
    print("m=",id(m))
    m[2][0] = 888
    print(m)
    print("m=",id(m))
f3(a)
print(a)  # 由于元组是不可变对象，所以元组的值是不可以改变的，但是元组中的列表是可以改变的

print("*"*100)
print()

#数的类型_位置参数_默认值参数_命名参数
 # 位置参数
def f21(a,b,c):
    print("a={0},b={1},c={2}".format(a,b,c),"位置参数")
f21(1,2,3)
 # 默认值参数
def f22(a,b,c=100):
    print("a={0},b={1},c={2}".format(a,b,c),"默认值参数")
f22(3,4)
 # 命名参数
def f23(a,b,c):
    print("a={0},b={1},c={2}".format(a,b,c),"命名参数")
f23(b=10,c=20,a=30)

print("*"*100)
print()

#参数的类型_可变参数_强制命名参数

# 可变参数   *c 代表可变参数
def f24(a,b,*c):
    print("a={0},b={1},c={2}".format(a,b,c),"可变参数")
f24(1,2,3,4,5,6,7,8,9)
# 强制命名参数
def f25(*c,a,b):
    print("a={0},b={1},c={2}".format(a,b,c),"强制命名参数")
f25(1,2,3,4,5,6,7,8,9,a=10,b=20)

def f26(a,b,**c):
    '''
    ** 是字典类型
    :param a:
    :param b:
    :param c:
    :return:
    '''
    print("a={0},b={1},c={2}".format(a,b,c),"** 是字典类型")

f26(1,2,x=100,y=200,z=300)

print("*"*100)
print()

# lambda表达式和匿名函数
# lambda表达式的定义  lambda 参数列表:表达式
f = lambda a,b,c:a+b+c

print(f(10,20,30),"f")

g = [lambda a:a*2,lambda b:b*3,lambda c:c*4]
print(g)
print(id(g))
print(type(g))
print(g[0](2),g[1](3),g[2](4),"g")

print("*"*100)
print()

#eval()函数的用法和注入安全隐患问题
s = "print('hello world')"
eval(s)

a = 10
b = 20
c = eval("a+b")
print(c)

dict1 = dict(a=100,b=200)
d1 = eval("a+b")
d = eval("a+b",dict1)   # 通过字典传递参数 与d1的值不同的原因是，d1是在全局变量中查找的
print(d,d1)

print("*"*100)
print()

#递归函数_函数调用内存分析_栈帧的创建

def my_resursion(n):
    print("start:"+str(n))
    if n == 1:
       print("resursion over")
    else:
        my_resursion(n-1)
    print("end:"+str(n))  # 递归函数的调用过程是一个栈帧的过程

my_resursion(9)

print("*"*100)
print()

#递归函数_阶乘计算案例
print("阶乘计算案例")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(500))

print("*"*100)
print()

#嵌套函数_内部函数_数据隐藏
