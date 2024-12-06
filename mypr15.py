#控制语句和现实逻辑表达
# 1.顺序结构 2.选择结构 3.循环结构

#单分支选择结构_条件表达式详解
 #选择结构：
    #单分支选择结构
    #if语句 if 条件表达式： 语句块
# num = input('输入一个整数：')
# if int(num) < 10:
#     print("num小于10的整数"+str(num))
#     print("num小于10的整数",str(num))

#条件表达式详解
# 条件表达式为false的情况：
    #0 0.0 '' None False

if 3:
    print("3为真")
# a = []
a = [1]
if a:
    print("a为真")

# b = ""
b='w'
if b:
    print("b为真")

if 'False':
    print("字符串False为真")

c = 9
if 0<c<10:
    print("0<c<10")

# e= False
# if e=False: #赋值语句不能作为条件表达式 -SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
#     print("e为真")


# 双分支选择结构_三元运算符的使用详解

# num = input('输入一个整数：')
# if int(num)<10:
#     print("num小于10的整数"+str(num))
# else:
#     print("num大于等于10的整数"+str(num))

#三元运算符
# x = input('输入一个整数：')
# a = x if int(x)<10 else '数字大于等于10' # x if 条件表达式 else y
# print(a)

#多分支选择结构
# score = int(input('输入一个分数：'))
# grade = ''
# if score>=90:
#     grade = '优秀'
# elif score>=80:
#     grade = '良好'
# elif score>=70:
#     grade = '中等'
# elif score>=60:
#     grade = '及格'
# else:
#     grade = '不及格'
# print("分数是{0},等级是{1}".format(score,grade))

# if score<60:
#     grade = '不及格'
# elif score<80:
#     grade = '及格'
# elif score<90:
#     grade = '中等'
# else:
#     grade = '优秀'
# print("分数是{0},等级是{1}".format(score,grade))

# x = int(input('输入x轴坐标：'))
# y = int(input('输入y轴坐标：'))
#
# if(x==0 and y==0):
#     print("坐标在原点")
# elif(x==0):
#     print("坐标在y轴上")
# elif(y==0):
#     print("坐标在x轴上")
# elif(x>0 and y>0):
#     print('坐标在第一象限')
# elif(x<0 and y>0):
#     print('坐标在第二象限')
# elif(x<0 and y<0):
#     print('坐标在第三象限')
# else:
#     print('坐标在第四象限')


#选择结构的嵌套
# score = int(input('输入一个在0-100之间的数字：'))
# grade = ""
# if score>100 or score<0:
#     score = int(input('输入错误！重新输入一个在0-100之间的数字：'))
# else:
#     if score>=90:
#         grade = '优秀'
#     elif score>=80:
#         grade = '良好'
#     elif score>=70:
#         grade = '中等'
#     elif score>=60:
#         grade = '及格'
#     else:
#         grade = '不及格'
#
# print("分数是{0},等级是{1}".format(score,grade))

# score = int(input('输入一个在0-100之间的数字：'))
# grade = "ABCDE"
# if score>100 or score<0:
#     score = int(input('输入错误！重新输入一个在0-100之间的数字：'))
# else:
#     asz = score//10 #
#     if asz<6:asz = 5
#     grade = grade[9-asz]
#     print("分数是{0},等级是{1}".format(score,grade))


#while循环结构_死循环处理
# num=0
# while num<=10:
#     print(num,' while循环')
#     num+=1
# print(num,' while循环结束')

num=1
sum=0
while 0<=num<=100:
    sum+=num
    num+=1

print(sum,' while循环结束')

#for循环结构_遍历各种可迭代对象_range对象
# for x in (20,30,40):
#     print(x*10,end=' ')
#
# for y in 'hello':
#     print(y,end=' ')
# d = {'name':'张','age':20,'address':'北京'}
# for k in d:
#     print(k,d[k]) #遍历字典的键值对
#
# for k in d.keys(): #遍历字典的键
#     print(k)
#
# for k in d.values(): #遍历字典的值
#     print(k)
#
# for k in d.items(): #遍历字典的键值对
#     print(k)

# for x in range(10):
#     print(x,end=' ')
#
# for x in range(3,11):
#     print(" ",x)
#
# for x in range(3,11,3):
#     print(" ",x)


# sum_nums = 0
# a_sums = 0
# b_sums = 0
#
# for nums in range(101):
#     sum_nums+=nums
# print(sum_nums)
#
# for nums in range(101):
#     if nums%2==0:
#         a_sums+=nums
#     else:
#         b_sums+=nums
# print(a_sums,b_sums)

#嵌套循环
for x in range(5):
    for y in range(5):
        print(x,end='\t')
    print() #换行

#嵌套循环练习_九九乘法表_打印表格数据

#先打印一行的 乘法表
# for n in (1,6):
#     print("{0}*{1}".format(5,n),end='\t')
# print()

#然后 再外层套大循环
# for m in range(1,10):
#     for n in range(1,m+1):
#         print("{0}*{1}".format(m,n),end='\t')
#     print()

#
# r1 = dict(name='高小一',age=18,salary=30000,city='北京')
# r2 = dict(name='高小二',age=19,salary=20000,city='上海')
# r3 = dict(name='高小三',age=20,salary=10000,city='深圳')
# tb = [r1,r2,r3]
# for i in tb:
#     if i.get('salary')>15000:
#         print(i)
#     print()

#break 语句 ---退出循环
# while True:
#     x = input('输入一个字符（exit 表示结束）：')
#     if x=='exit':
#         break
#         print(x)
#     else:
#         print(x)


#continue 语句 ---跳过当前循环,继续下一次循环
# empNum = 0
# salarys = []
# salarySum = 0
# while True:
#     s = input('请输入员工的薪资（按Q或q结束）:')
#     if s.upper()=='Q':
#         print('录入完成，退出！')
#         break
#     if float(s)<0:
#         print('录入错误，薪资不能为负数！请重新录入')
#         continue
#     print('录入成功！')
#     empNum+=1
#     salarys.append(float(s))
#     salarySum+=float(s)
# print('员工人数为：{0}，薪资总和为：{1}，平均薪资为：{2}'.format(empNum,salarySum,salarySum/empNum))


#循环中的else语句(while,for)
# salarySum = 0
# salarys = []
# for i in range(4):
#     s = input('请输入4名员工的薪资（按Q或q结束）:')
#     if s.upper()=='Q':
#         print('录入完成，退出！')
#         break
#     if float(s)<0:
#         print('录入错误，薪资不能为负数！请重新录入')
#         continue
#     print('录入成功！')
#     salarySum+=float(s)
#     salarys.append(float(s))
# else:
#     print('所有员工的薪资录入成功！')
#
# print('录入的薪资为：',salarys)
# print('录入的薪资总和为：',salarySum)
# print('录入的薪资平均值为：',salarySum/4)

#循环代码优化技巧
import time
start = time.time()
for i in range(1000):
    result = []
    for m in range(10000):
      c = i*1000
      # result = result + [m*100] #不要使用+号，会生成新的列表对象
      result.append(c+m*100) #使用append方法，只是在原列表对象上添加元素
end = time.time()
print('耗时：',end-start)

print('优化后的')

start = time.time()
for i in range(1000):
    result = []
    c = i * 1000
    for m in range(10000):
      # result = result + [m*100] #不要使用+号，会生成新的列表对象
      result.append(c+m*100) #使用append方法，只是在原列表对象上添加元素
end = time.time()
print('耗时：',end-start)

#zip()并行迭代多个序列
# names = ['张三','李四','王五','赵六']
# ages = [20,30,40,50]
# jobs = ['工程师','医生','律师']
#
# for name,age,job in zip(names,ages,jobs):
#     print('{0}--{1}--{2}'.format(name,age,job))

#非zip实现方式
names = ('张三','李四','王五','赵六')
ages = (20,30,40,50)
jobs = ('工程师','医生','律师')

for i in range(min(len(ages),len(ages),len(jobs))):
    print('{0}--{1}--{2}'.format(names[i],ages[i],jobs[i]))

#推导式创建序列_列表推导式_字典推导式_集合推导式_生成器推导式
   #列表推导式
ls = [x*6 for x in range(10) if x%2==0]
print(ls,'推导式')

lsb = []
for x in range(1,10):
    if x%2==0:
        lsb.append(x*6)
print(lsb,'非推导式')

#字典推导式
values = ['北京','上海','深圳','广州']
cities = {id:city for id,city in zip(range(1,5),values)}
print(cities,'字典推导式')

my_text = 'I love python programming I love javascript programming I love java programming'
char_count = {s:my_text.count(s) for s in my_text}
print(char_count,'字典推导式')

#集合推导式
os_a = {x for x in range(10) if x%2!=0}
print(os_a,'集合推导式')

#生成器推导式
g = (x for x in range(1,100) if x%9==0) #生成器对象
print(g,'生成器推导式')

for x in g:
    print(x,end=' ')

for x in g:
    print(x,end=' ')   #生成器对象只能迭代一次

# 综合练习_绘制不同颜色的同心圆_绘制棋盘
import turtle
p = turtle.Pen() #创建画笔对象
# p.circle(10) #绘制半径为100的圆
# p.penup() #抬起画笔
# p.goto(0,-10) #移动到坐标(0,-10)    #绘制同心圆
# p.pendown() #放下画笔
# p.circle(20)
radius = [x*10 for x in range(1,11)]
colors = ['red','green','yellow','black']
p.width(4) #设置画笔宽度
for i,color_j in zip(radius,range(len(radius))):
    p.penup() #抬起画笔
    p.goto(0,-i) #移动到坐标(0,-i)
    p.pendown() #放下画笔
    # p.pencolor(colors.pop()) #设置画笔颜色
    p.color(colors[color_j%len(colors)]) #设置画笔颜色
    p.circle(i) #绘制圆

turtle.done()