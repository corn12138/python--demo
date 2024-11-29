#split 和 join 方法
#split() 方法通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
#join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串

#split() 方法语法：
a = "hello,world"
b=a.split(",")
print(b)

#join() 方法语法：
c = ['hello', 'world']
d = ','.join(c)
print(d)

#split() 方法和 join() 方法是一对互逆操作，可以用来实现很多字符串操作。

import time

time1 = time.time()
s=""
for i in range(1000000):
    s+="cdx"
time2 = time.time()
print("+=",time2-time1)

time3 = time.time()
l = []
for i in range(1000000):
    l.append("cdx")
s = "".join(l)
time4 = time.time()
print("join",time4-time3)