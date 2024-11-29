a = True
b = False
c = a and b
print(c)
d = a or b
print(d)
e = not (a or b)
print(e)


#
f= 10<30 and 10<100
g =100>200 and 50<(3/0) #发生短路
h=100
i = 50<h<500
print(f,g,i)

s= 'hello '
print(s*89)
