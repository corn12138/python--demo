#字符串的replace 方法--替换字符串中的子串

a = "abcdefghigklmnopqrstuvwxyzd"
# a[3] = '第' #字符串是不可变的，不能通过索引修改字符串中的字符
# print(a)
b=a.replace('d','第') #replace 方法返回一个新的字符串，原字符串不变
print(a)
print(b)

#replace 方法的第三个参数，指定替换的次数
c=a.replace('d','第',1)  #只替换第一个d
print(c)

print(a[1],a[-2])