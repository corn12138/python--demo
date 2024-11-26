import turtle

#第一个圆
turtle.width(10)
turtle.color('blue')
turtle.circle(60)


#第二个圆
turtle.penup()
turtle.goto(140,0)
turtle.pendown()
turtle.color('black')
turtle.circle(60)


#第三个圆
turtle.penup()
turtle.goto(280,0)
turtle.pendown()
turtle.color('red')
turtle.circle(60)

#第四个圆
turtle.penup()
turtle.goto(70,-70)
turtle.pendown()
turtle.color('yellow')
turtle.circle(60)

#第五个圆
turtle.penup()
turtle.goto(210,-70)
turtle.pendown()
turtle.color('green')
turtle.circle(60)

turtle.done();  #表示 窗口一直存在