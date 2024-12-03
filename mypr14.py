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
# 字典的创建
a = {"name":"zs",'age':19,'job':'programmer'}
print(a,'字典')
print(a['name']) # 通过键访问字典中的值

b = dict(name='ls',age=20,job='teacher') # 通过关键字参数创建字典
print(b,'字典2')

c = dict([('name','ww'),('age',21),('job','doctor')]) #
# 通过列表创建字典
print(c,'字典3')

k = ['name','age','job']
v= ['zl',22,'driver']
print(list(zip(k,v)),'zip')
d = dict(zip(k,v)) # 通过zip()函数创建字典 --zip()函数将多个序列中的元素一一对应，返回一个元组的列表
print(d,'字典4')

e= dict.fromkeys(['name','age','job']) #
# 通过fromkeys(
# )方法创建字典
print(e,'字典5')

# 字典_元素的访问_键的访问_值的访问_键值对的访问

print(a['name'],'元素访问') # 通过键访问字典中的值
print(b.get('name'),'元素的访问') # 通过get()方法访问字典中的值
# ---若键不存在，返回None
print(a.get('gender','a man')) # 若键不存在，返回指定的默认值

print(a.items()) # items()方法返回字典中的键值对
print(a.keys()) # keys()方法返回字典中的键
print(a.values()) # values()方法返回字典中的值
print(len(a)) # len()方法返回字典中键值对的个数
print('gender' in a) # in 判断键是否在字典中



#字典_元素的添加_修改_删除
#字典元素的添加

a['address'] = 'beijing' # 添加一个新的键值对
a['age'] = 90 # 修改键值对的值
print(a,'添加修改1')
g = {'name':'sd','age':342,'job':'sdf','cs':'erxewqwe'}
a.update(g)
print(a,'添加修改2') # update()方法将一个字典中的键值对添加到另一个字典中

#字典元素的删除
# del a['job'] # del 删除指定键值对
# ages = a.pop('age') # pop 删除指定键值对，并返回该键值对的值
# print(a,'删除1',ages)
# a.clear() # clear()方法清空字典
# print(a)
# a.popitem() # popitem()方法随机删除字典中的一个键值对
# print(a,'删除2')

#字典_序列解包用于列表元组字典
# 序列解包用于列表
u,v,w = [1,2,3]
print(u,v,w)
# 序列解包用于元组
x,y,z = (4,5,6)
print(x,y,z)
# 序列解包用于字典
s={'name':'zs','age':19,'job':'programmer'}
# m,n,o =  s
# print(m,n,o,'字典解包')
m,n,o = s.items() # items()方法返回字典中的键值对
print(m[0],m[1],n[0],n[1],o[0],o[1],'字典解包1')
# m,n,o = s.values() # values()方法返回字典中的值
# print(m,n,o,'字典解包2')


#字典_复杂表格数据存储_列表和字典综合嵌套

r1 = {'name':'zs','age':19,'job':'programmer',
      'salary':10000,'city':'beijing'}
r2 = {'name':'ls','age':20,'job':'teacher','salary':20000,'city':'shanghai'}
r3 = {'name':'ww','age':21,'job':'doctor','salary':30000,'city':'guangzhou'}

tb = [r1,r2,r3] # 列表中的元素是字典
print(tb,'表格数据')
for i in range(len(tb)):
    print(tb[i].get('salary','no salary'),tb[i].get(
        'name'),tb[i].get('age'),tb[i].get('city')) # get(
    # )方法访问字典中的值


#字典_核心底层原理_内存分析_存储键值对过程
 # 字典核心底层原理
    # 字典是一种无序的数据结构，字典中的元素是键值对，键是唯一的，值可以重复



#字典_核心底层原理_内存分析_查找值对象过程




#集合_特点_创建和删除_交集并集差集运算
    #集合是一种无序的数据结构，集合中的元素是唯一的，不重复

a = {10,20,30,40,50}
b = {100,200,30,400,500}
# c = a|b # |并集运算
# d = a&b # &交集运算
# e = a-b # -差集运算
c = a.union(b) # union()方法并集运算
d = a.intersection(b) # intersection()方法交集运算
e = a.difference(b) # difference()方法差集运算
print(c,d,e)

#集合和字典有何关系
    #相同的
        #集合和字典都是无序的数据结构
        #两者都是使用hash表作为底层实现，这使得它们的查找、添加、删除操作的时间复杂度都是O(1)
        #它们都是只能包含不可变的对象作为键或者元素。
        #都是 {} 包裹
        
        # 不同点
          #创建方式：
            # 字典:使用{} 并包含键值对， {‘a’:2,'b':3}
            # 集合:使用{} 或set()并包含元素， {1,2,3}
          #结构：
            #字典：包含键值对
            #集合：只包含元素
          #用途：
            #字典：存储键值对的映射关系
            #集合：存储唯一元素，用于去重
          #索引：
            #字典：通过键访问值 
            #集合：不支持索引和访问
           
          #方法和操作：
            #字典：items() keys() values() get() pop() update() clear() popitem()
            #集合：union() intersection() difference() add() remove() discard() clear() pop()



#元组与列表的相同点和不同点
  #相同点
    #元组和列表都是序列类型：可以按照索引访问元素，可以进行切片操作
    #都可以存储任何类型的数据
    #都支持嵌套操作：可以包含其他元组和列表
    #都支持序列解包
    #都可以使用len()函数获取长度
    # 都可以使用 in 和 not in 判断元素是否在序列中
    # 都可以使用 + 和 * 运算符进行拼接和重复操作
    
  #不同点
    #可变性：
        #元组是不可变的，元组的元素不能修改，删除，添加
        #列表是可变的，列表的元素可以修改，删除，添加
    #语法：
        #元组使用()包裹元素，列表使用[]包裹元素
        
    #方法：
        #元组没有append() extend() insert() remove() sort() reverse()等方法
        #列表有append() extend() insert() remove() sort() reverse()等方法
        
    #性能：
        #元组通常比列表占用更少的内存
        #元组的访问速度比列表更快
        
     #适用场景：
        #元组适用于存储不需要修改的数据，或者存储异构数据
        #列表适用于存储需要修改的数据
        
     #哈希性：
        #元组是可哈希的，可以作为字典的键，也可以作为集合的元素
        #列表是不可哈希的，不能作为字典的键，也不能作为集合的元素
        
     #创建空序列：
        #元组使用()创建空元组
        #列表使用[]创建空列表
        


a = [
    ['高小一',18,30000,'北京'],
    ['高小二',19,20000,'上海'],
    ['高小五',20,10000,'深圳']
]

for i in a:
    for j in i:
        print(j,end="\t")
    print()
    
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))