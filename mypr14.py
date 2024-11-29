# 序列

# 序列的本质和内存结构

# 序列是一种数据结构，用于存储多个数据元素，每个元素都有一个唯一的序号，称为索引，通过索引可以访问序列中的元素。

# 列表简介

# 列表的创建
a=list(range(10))
print(type(a),a)
b = list(range(3,15,2)) # 从3开始，到15结束，步长为2
print(b)

# 列表的操作
d = [x*2 for x in range(0,30,2) if x%3!=0]
print(d,"for循环生成列表")

#列表元素的增加
l=[1,2,3]
print(id(l))
l.append(4) # 在列表末尾添加一个元素
print(id(l),l,"append")
l.extend([6,7,8]) # 在列表末尾添加多个元素
print(id(l),l,"extend")
l.insert(1,5) # 在指定位置插入一个元素
print(id(l),l,"insert")
# append extend insert 不生成新的列表，直接在原列表上进行操作

l+=[5] # 在列表末尾添加一个元素--加法扩展生成新的列表

print(id(l),l,"+")
k=l*4 #*生成新的列表--乘法扩展
print(id(k),k,"*")



# 列表元素的删除
# del 删除指定位置的元素
# pop 删除指定位置的元素，并返回该元素的值,若未指定位置，则删除最后一个元素
# remove 删除首次出现的 指定值的元素，若有多个相同值的元素，只删除第一个，若没有指定值的元素，则报错
arrs = [1,2,3,4,5,6,7,8,9]
# del arrs[1]
# arrs.pop(2)
# arrs.pop()
# arrs.remove(9)


# 列表元素的访问 -- 出现次数统计 -- 成员资格判断
 #索引访问
lisy = [1,2,3,4,5,6,7,8,9]
print(lisy[2],lisy[5])
 # index()方法获取指定元素在列表中首次出现的索引
print(lisy.index(3),"index")
    # count()方法获取指定元素在列表中出现的次数
print(lisy.count(3),"count")
    # len()方法获取列表中元素的个数
print(len(lisy),"len")
    # in 和 not in 判断元素是否在列表中
print(3 in lisy,3 not in lisy)


# 列表的切片操作--slice
# 切片操作是对列表中的元素进行切片，返回一个新的列表   --silce[start:stop:step]

lik = [1,2,3,4,5,6,7,8,9]
print(lik[1:5:2],"slice")   # 从索引1开始，到索引5结束，步长为2
print(lik[1:5],"slice")       # 从索引1开始，到索引5结束，步长为1
print(lik[:5],"slice")        # 从索引0开始，到索引5结束，步长为1
print(lik[1:],"slice")          # 从索引1开始，到列表末尾结束，步长为1
print(lik[:],"slice")          # 从索引0开始，到列表末尾结束，步长为1
print(lik[::2],"slice")         # 从索引0开始，到列表末尾结束，步长为2
print(lik[::-1],"slice")         # 从索引0开始，到列表末尾结束，步长为-1，逆序输出--反转列表


# 列表的 遍历 复制 排序

lok = [10,20,30,40]
for i in lok:                # 遍历列表
    print(i,end=" ")    # end = " " 使输出不换行
    
# 复制列表
# loks = lok
loks = []+lok                 # +生成新的列表
print(lok is loks)  # is 判断两个变量是否指向同一个对象
lok1 = lok.copy()  # copy()方法复制列表
print(lok is lok1,lok1)

# 排序
lokop = [20,10,40,30]
# lokop.sort() # sort()方法对列表进行排序
lokop.sort(reverse=False) # sort(reverse=True)方法对列表进行逆序排序
print(lokop)

import random # 导入random模块
random.shuffle(lokop) # shuffle()方法对列表进行随机排序
print(lokop,"shuffle")

#sorted()函数对列表进行排序，不改变原列表
ops = [20,10,40,30]
ops1 = sorted(ops)
print(ops1,"sorted")

#reversed()函数对列表进行逆序排序，不改变原列表

# max min sum 函数 -- 求列表中的最大值 最小值 求和
print(max(ops),min(ops),sum(ops))



# 列表_二维列表_表格数据存储和读取
# 二维列表是列表中的元素也是列表，可以用来存储表格数据
at = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in at:
    for j in i:
        print(j,end="\t")
    print()



# 元组_特点_创建的两种方式_tuple()要点
# 元组是一种不可变的序列，元组的元素不能修改，删除，添加
# 元组的创建
tas = (1,2,3)
tbs = 4.5,6
tcs = (100,)
tds = (100)
print(type(tas),tas)
print(type(tbs),tbs)
print(type(tcs),tcs)
print(type(tds),tds)

# tuple()函数创建元组
tes = tuple()     # 创建一个空元组
tfs = tuple(range(10))  # 创建一个包含0~9的元组
tgs = tuple("jksd")  # 创建一个包含字符串中字符的元组
ths = tuple([7,8,9]) # 创建一个包含列表中元素的元组
print(tes,tfs,tgs,ths)

#元组_元素访问_计数方法_切片操作_成员资格判断_zip()函数
#元组元素的访问--参考列表
#元组元素的计数方法--参考列表

a = (1,2,3,4,5,6,7,8,9)
b = sorted(a) # sorted()函数对元组进行排序

# zip()函数将多个序列中的元素一一对应，返回一个元组的列表
c = [1,2,3]
d = [4,5,6]
e = [7,8,9]
f = zip(c,d,e) # zip()函数将多个序列中的元素一一对应，返回一个元组的列表
print(f)
print(list(f))

#元组_生成器推导式创建元组_总结
#生成器推导式创建元组
_ge = (x for x in range(10))
print(_ge)
_gs = tuple(_ge)
print(_gs)
_s =tuple(_ge)  # 生成器只能使用一次,再次使用时为空。
print(_s)
         # next()函数获取生成器中的下一个元素
_e = (x for x in range(3))
print(_e.__next__())
print(_e.__next__())
print(_e.__next__())
# print(_e.__next__())# 报错



# 字典_特点_4种创建方式_普通_dict_zip_fromkeys
# 字典是一种无序的数据结构，字典中的元素是键值对，键是唯一的，值可以重复



