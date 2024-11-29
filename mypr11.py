#字符串的slice操作
#字符串的slice操作是一种非常强大的操作，可以让我们快速获取字符串的某一部分。
# slice(start, end)函数，它接受两个参数，start表示起始位置，end表示结束位置，然后返回从start到end的子串。  
#比如，取一个字符串的前3个字符，只需要简单的操作：
a = "abcedfghigklmnopqrstuvwxyz"
print(a[0:3])
print(a[-3:])