import turtle

turtle.showturtle() #显示箭头
turtle.write('hym,你好！') #在窗口中写字
turtle.forward(300) #前进300像素
turtle.color('violet') #改变画笔的颜色
turtle.left(90) #箭头左转90度
turtle.forward(300) #前进300像素
turtle.goto(0,0) #回到原点
turtle.penup() # 抬笔 不用画路径
turtle.goto(0,50) #移动到坐标(0,50)
turtle.pendown() # 下笔
turtle.circle(100) #半径为100的圆

turtle.done(); #表示 窗口一直存在