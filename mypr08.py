#字符串基本特点

    #字符串是不可变的
    #字符串是有序的
    #字符串的编码方式--->ASCII,Unicode,UTF-8
    # ord()函数：返回字符的ASCII码 chr()函数：返回ASCII码对应的字符
a= ord('A')
print(a,ord('黄'),chr(65),chr(20013))
    #字符的创建方式 -  单引号，双引号，三引号
s = '''hello

        world'''
print(s)
    #空字符串 -  一个字符串不包含任何字符，它的长度为0
m = ''
print(len(m))
    #字符串的拼接 -  使用+号

