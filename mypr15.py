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

x = int(input('输入x轴坐标：'))
y = int(input('输入y轴坐标：'))

if(x==0 and y==0):
    print("坐标在原点")
elif(x==0):
    print("坐标在y轴上")
elif(y==0):
    print("坐标在x轴上")
elif(x>0 and y>0):
    print('坐标在第一象限')
elif(x<0 and y>0):
    print('坐标在第二象限')
elif(x<0 and y<0):
    print('坐标在第三象限')
else:
    print('坐标在第四象限')


