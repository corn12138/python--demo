class MyRectangle:
    '''
    这个类用于描述一个矩形
    '''
    # 构造方法
    def __init__(self,x=0,y=0,width=100,height=100):
        self.x = float(x)
        self.y = float(y)
        self.width = float(width)
        self.height = float(height)


    #计算矩形的面积
    def getArea(self):
        return self.width * self.height

    #计算矩形的周长
    def getPerimeter(self):
        return 2*(self.width + self.height)

    #海龟绘图
    def draw(self):
        import  turtle
        p = turtle.Pen()
        p.penup()
        p.goto(self.x,self.y)   #移动到指定位置
        p.pendown()
        p.goto(self.x + self.width,self.y)# x轴方向
        p.goto(self.x+self.width,self.y+self.height) # y轴方向
        p.goto(self.x,self.y+self.height)
        p.goto(self.x,self.y) # 回到原点
        turtle.done() #结束绘图


p1 = MyRectangle(-2,3,9.8,10)
print(p1.getArea(),"面积")
print(p1.getPerimeter(),"周长")
p1.draw()

