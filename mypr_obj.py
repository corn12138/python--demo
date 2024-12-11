# 面向对象

#面向对象和面向过程的区别_设计者思维_执行者思维

# 面向对象的三大特性：封装、继承、多态
# 封装：将数据和方法封装在一起，对外提供接口
# 继承：子类继承父类的属性和方法
# 多态：不同的子类对象调用相同的方法，产生不同的结果
# 面向对象的设计原则：单一职责原则、开闭原则、里氏替换原则、依赖倒置原则、接口隔离原则、迪米特法则
# 面向对象的设计模式：单例模式、工厂模式、观察者模式、装饰者模式、适配器模式、代理模式、策略模式、模板方法模式、迭代器模式、组合模式、状态模式、责任链模式、命令模式、访问者模式、备忘录模式、解释器模式、中介者模式、享元模式、桥接
# 面向对象与面向过程的区别：面向对象是设计者思维，面向过程是执行者思维

#对象进化的小故事
'''
# 1.0
'''
from time import clock_settime


#类的定义_类和对象的关系_对象的内存模型
#类的定义: class 类名: 类名的命名规则和变量的命名规则一样，首字母大写，多个单词使用驼峰命名法
# 属性和方法：属性是类的特征，方法是类的行为
#类和对象的关系: 类是对象的模板，对象是类的实例

class Student:
    '''
    学生类
    self: 表示类的实例，类的方法的第一个参数必须是self
    __init__: 初始化方法，创建对象时自动调用
    pass: 表示空实现，没有实际功能
    '''
    def __init__(self,name,score):
        self.name = name
        self.score = score
        pass
    def say_score(self):
        print("{0}的分数是{1}".format(self.name,self.score))

s1 = Student('张三',100)
print(s1.name,s1.score)

s2 = Student('李四',90)
print(s2.name,s2.score)

s1.say_score()
s2.say_score()

print("*"*100)
print()

#构造函数_init和new方法
#构造函数__init__: 创建对象时自动调用，初始化对象的属性,默认不写时，会自动调用object的__init__方法
#new方法__new__: 创建对象时自动调用，返回对象的引用，默认不写时，会自动调用object的__new__方法

#实例属性_内存分析
 #实例属性: 对象的属性，通过对象访问
class Students:
    '''
    学生类
    self: 表示类的实例，类的方法的第一个参数必须是self
    __init__: 初始化方法，创建对象时自动调用
    pass: 表示空实现，没有实际功能
    '''
    def __init__(self,name,score):
        self.name = name #新增name属性
        self.score = score #新增score属性
        pass
    def say_score(self):
        self.age = 18 #新增age属性--实例属性
        print("{0}的分数是{1}".format(self.name,self.score))


s3 = Students('张三',100)
s3.say_score()
print(s3.name,s3.score,s3.age)

s4 = Students('李四',90)
s4.address = '北京' #新增address属性
print(s4.name,s4.score,s4.address)

print("*"*100)
print()

#实例方法_内存分析方法调用过程_dir()_isinstance

class StudentsTest:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def say_score(self,c):
        self.age = 18
        print("{0}的分数是{1}".format(self.name,self.score))
        print(c)

a = StudentsTest("张三",90)
# a.say_score(68)
StudentsTest.say_score(a,68) #等价于a.say_score(68)

print(dir(a)) #查看对象的属性和方法
print(isinstance(a,StudentsTest)) #判断对象是否是指定类的实例
print(a.__dict__,"查看对象的属性和值") #查看对象的属性和值
print(StudentsTest.__dict__) #查看类的属性和值

print("*"*100)
print()

#类对象

class TesCls:
    pass
print(type(TesCls)) #<class 'type'> 类型
print(id(TesCls)) #对象的内存地址
print(TesCls)

class Car:
    pass
Stu = TesCls
s = Stu()
print(s)

print("*"*100)
print()

#类属性_内存分析(创建类和对象的底层原理)
    #类属性: 类的属性，通过类访问--类属性是所有对象共享的
class Studentss:
    company = "sxt"
    count = 0

    def __init__(self,name,score):
        self.name = name
        self.score = score
        Studentss.count += 1
        pass
    def say_score(self):
        print("{0}的分数是{1}".format(self.name,self.score))
        print("count:",Studentss.count)
m1 = Studentss("张三",100)
m2 = Studentss("李四",90)
m1.say_score()

print("*"*100)
print()

#类方法_静态方法
    #类方法: 通过类调用的方法，第一个参数是cls，表示类本身
    #静态方法: 通过类调用的方法，没有默认
class Std:
    '''
    学生类
    '''
    company = "sxt"

    def __init__(self,name):
        self.name = name
        pass

    @classmethod
    def print_company(cls):
        print(cls.company)

    @staticmethod
    def add(a,b):    #静态方法--不需要self和cls--可以通过类名直接调用
        print("{0}+{1}={2}".format(a,b,a+b))
        return a+b

Std.print_company()
Std.add(1,2)

print("*"*100)
print()

#del析构方法_垃圾回收机制简介
    #析构方法: 对象销毁时自动调用
    #垃圾回收机制: Python自动回收不再使用的对象
# class Person:
#      def __del__(self):
#          print("销毁对象{0}".format(self))

# p1 = Person()
# del p1   #手动销毁对象
# p2 = Person()
# print("程序结束")


print("*"*100)
print()

#call方法和可调用对象
    #call方法: 对象后面加括号，自动调用call方法
    #可调用对象: 对象后面加括号，自动调用call方法
def f1():
    print("f1")

print(f1)
print(id(f1))
print(type(f1))
f1()
print(dir(f1),"dir")

class Cars:
    '''
    __call__: 对象后面加括号，自动调用call方法
    '''
    def __call__(self, age,money):
        print("call方法被调用")
        print("车龄:{0},金额:{1}".format(age,money))

c = Cars()
c(3,2000000)

print("*"*100)
print()

#方法没有重载_方法的动态性
    #方法没有重载: Python不支持方法重载 --- 同名方法会覆盖--后面的方法会覆盖前面的方法
    #方法的动态性: 可以在程序运行时动态添加方法
class Personse:
    '''
    方法的动态性
    '''
    def work(self):
        print("努力工作")

def play_games(s):
    print("玩游戏")
def work2(s):
    print("好好学习")

Personse.play = play_games
Personse.work = work2

Personse().play()
Personse().work()

print("*"*100)
print()

#私有属性--私有方法
    #私有属性: 属性名前加两个下划线__，表示私有属性
    #私有方法: 方法名前加两个下划线__，表示
class Employee:
    '''
    私有属性和私有方法
    '''
    __company = "sxt" # 私有属性--解释器运行时把__company变成_Employee__company

    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def say_company(self):
        print("公司名称:{0}".format(Employee.__company))
        print("年龄:{0}".format(self.__age))
    def __mywork(self):
        print("工作")
ps1 = Employee("张三",18)
ps1.say_company()
# ps1.__mywork() #私有方法不能在外部调用
print(dir(Employee))
# print(Employee._Employee__company) #_类名__私有属性名

print("*"*100)
print()

#@property装饰器 --- 把方法变成属性
    #@property: 把方法变成属性，调用方法时不需要加括号
    #setter: 设置属性值
    #deleter: 删除属性
class Employees:
    '''
    @property装饰器--把方法变成属性
    '''
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        print("月薪资:",self.__salary)
        return self.__salary
    @salary.setter  # 设置属性值
    def salary(self,salary):
        if 0<salary<1000000:
            self.__salary = salary
        else:
            print("薪资录入错误")

emp1 = Employees("张三",100000)

emp1.salary = 200000  #调用setter方法
print(emp1.salary)
# emp1.salary()

print("*"*100)
print()

#属性和类的命名规则总结
    #属性和方法的命名规则: 驼峰命名法
    #类的命名规则: 首字母大写，多个单词使用驼峰命名法
    #私有属性和私有方法: 属性名前加两个下划线__，方法名前加两个下划线__
    #类属性和类方法: 类属性和类方法通过类名访问，类方法的第一个参数是cls
    #静态方法: 通过类名访问，不需要self和cls
    #可调用对象: 对象后面加括号，自动调用call方法
    #属性装饰器: 把方法变成属性，调用方法时不需要加括号
    #setter: 设置属性值
    #deleter: 删除属性

#None 对象的特殊性
    #None: 表示空对象，表示什么都没有
    #is: 判断两个对象是否是同一个对象
    #==: 判断两个对象的值是否相等
    # 注意：None是Python中的一个对象，不是关键字，
    # 注意2:None 不是False, None 不是0, None 不是空字符串
    #None和任何其他的数据类型比较都是False
obj = None
obj2 = None
print(type(None))
print(id(None))
print(id(obj))
print(id(obj2))

a = None
if a is None and a == None:
    print("a是None")
if a ==False or a ==0:
    print("a是False或0")   #None和任何其他的数据类型比较都是False

a1 = []; a2 =(); a3 = ""; a4 = 0; a5 = None
if(not a) and (not a1) and (not a2) and (not a3) and (not a4) and (not a5):
    print("if 判断时，空列表，空元组，空字符串，0，None都转换为False")

if (a1==False or a3==False):
    print("==时,空列表和空字符串不等于False")  #不会执行
if(a4==False):
    print("==时,0等于False")

print("*"*100)
print()

#面向对象的三大特征说明(封装、继承、多态)
    #封装: 将数据和方法封装在一起，对外提供接口
    #继承: 子类继承父类的属性和方法
    #多态: 不同的子类对象调用相同的方法，产生不同的结果

#继承详解
    #继承: 子类继承父类的属性和方法
    #子类: 继承父类的类
    #父类: 被继承的类
    #继承的好处: 提高代码的复用性
    #继承的原则: 子类是父类的一种特殊情况
    #继承的语法: class 子类名(父类名):
    #super(): 调用父类的方法
    #重写: 子类重写父类的方法
    #多继承: 一个子类有多个父类
    #继承的顺序: 从左到右，深度优先

class Person:
    '''
    父类
    '''
    def __init__(self,name,age):
        print("创建Person对象")
        self.name = name
        self.age = age
    def say_age(self):
        print("{0}的年龄是{1}".format(self.name,self.age))

class Student(Person):
    '''
    子类
    '''
    def __init__(self,name,age,score):
        super().__init__(name,age)    #调用父类的方法
        # super().say_age()
        # Person.__init__(self,name,age)    #调用父类的方法
        print("创建Student对象")
        self.score = score

    def say_score(self):
        print("{0}的分数是{1}".format(self.name,self.score))

sl1 = Student("张三",18,100)
sl1.say_age()
sl1.say_score()
print(dir(sl1))

print("*"*100)
print()

#成员继承和方法的重写
    #成员继承: 子类继承父类的属性和方法
    #方法的重写: 子类重写父类的方法
class Persons:
    '''
    父类
    '''
    def __init__(self,name,age):
        print("创建Person对象")
        self.name = name
        self.__age = age
    def say_age(self):
        print("{0}的年龄是{1}".format(self.name,self.__age))

    def say_name(self):
        print("我是{0}".format(self.name))

class Students(Persons):
    '''
    子类
    '''
    def __init__(self,name,age,score):
        super().__init__(name,age)    #调用父类的方法
        print("创建Student对象")
        self.score = score
    def say_score(self):
        print("{0}的分数是{1}".format(self.name,self.score))
    def say_name(self): #重写父类的方法
        print("报告老师,我是{0}".format(self.name))

sl2 = Students("张三",18,100)
sl2.say_score()
sl2.say_name()
sl2.say_age()

class A:pass
class B(A):pass
class C(B):pass

print(C.mro()) #查看类的继承顺序

print("*"*100)
print()

#object根类_查看模块结构_dir()

class Person:
    '''
    父类
    '''
    def __init__(self,name,age):
        print("创建Person对象")
        self.name = name
        self.age = age
    def say_age(self):
        print("{0}的年龄是{1}".format(self.name,self.age))

obj = object()
print(dir(obj))

s2 = Person("李四",20)
print(dir(s2))
print(s2.say_age)
print(type(s2.say_age))

print("*"*100)
print()

#重写str方法
class Persons:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        '''
        重写str方法-- 将对象转化为一个字符串，一般用于print方法
        :return:
        '''
        print("重写__str__方法")
        return "{0}的年龄是{1}".format(self.name,self.age)


p = Persons("张三",18)
print(p)
s = str(p)
print(s)

print("*"*100)
print()

#多重继承
    #多重继承: 一个子类有多个父类
    #继承的顺序: 从左到右，深度优先--查找属性和方法时，按照继承的顺序查找
    # 尽量避免多重继承
    #super():
class A:
    def aa(self):
        print("aa")

class B:
    def bb(self):
        print("bb")

class C(A,B):
    def cc(self):
        print("cc")

c = C()
c.cc()
c.bb()
c.aa()
print(C.mro())

print("*"*100)
print()

#MRO方法解析顺序
class A:
    def aa(self):
        print("aa")

    def say(self):
        print("say AAA!")
class B:
    def bb(self):
        print("bb")

    def say(self):
        print("say BBB!")


class C(B, A):

        def cc(self):
            print("cc")

c = C()
print(C.mro())
c.say()
    # 打印类的层次结构
    # 解释器寻找方法是“从左到右”的方式寻找，此时会执行B类中的say()

print("*"*100)
print()

#super()获得父类的定义
    #super(): 获得父类的定义
    #super()和__mro__: super()是根据__mro__的顺序来查找的
    #super()和多重继承: super()和多重继承的顺序有关

class A:
    def __init__(self):
        print("A的构造方法")

    def say(self):
        print("A=>",self)
        print("say AAA!")

class B(A):
    def __init__(self):
        # A.__init__(self)
        super().__init__() #调用父类的构造方法
        print("B的构造方法")

    def say(self):
        super().say() #调用父类的方法
        print("say BBB!")

b = B()
b.say()

print("*"*100)
print()

#多态详解
    #多态: 不同的子类对象调用相同的方法，产生不同的结果
    #多态的好处: 提高代码的灵活性
    #多态的原则: 子类是父类的一种特殊情况
    #多态的实现: 重写父类的方法

class Animal:
    def shout(self):
        print("动物叫")

class Dog(Animal):
    def shout(self):
        print("汪汪汪")

class Cat(Animal):
    def shout(self):
        print("喵喵喵")

def animalShout(a):
    a.shout() # 多态,传入的对象不同，调用的方法不同

animalShout(Dog())
animalShout(Cat())

print("*"*100)
print()

#特殊方法和运算符重载
    #特殊方法: __方法名__，Python的内置方法
    #运算符重载: 重写特殊方法，实现运算符重载
    #运算符重载的原则: 不能重载内置方法，只能重载特殊方法
    #运算符重载的好处: 提高代码的灵活性
    #运算符重载的实现: 重写特殊方法

a = 20
b = 30
c = a+b
d = a.__add__(b)

print(c,d)

class Person:
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        if isinstance(other,Person):
            return "{0}{1}".format(self.name,other.name)

    def __mul__(self, other):
        if isinstance(other,int):
            return self.name*other
        else:
            return "不是同类对象 不能相乘"

p1 = Person("张三")
p2 = Person("李四")

print(p1+p2)

print(p1*3)

print("*"*100)
print()

#特殊属性
    #特殊属性: __属性名__
    #特殊属性的作用: 用于实现特殊功能
    #特殊属性的实现: 重写特殊属性
    #特殊属性的使用: 通过对象访问
    #特殊属性的分类: __doc__,__name__,__module__,__class__

class A:
    pass

class B:
    pass

class C(B,A):
    '''
    类的说明

    '''
    def __init__(self,nn):
        self.nn = nn

    def cc(self):
        print("cc")


c = C(3)

print(c.__dict__) #查看对象的属性和值
print(c.__class__) #查看对象所属的类
print(C.__bases__) #查看类的父类
print(C.mro()) #查看类的继承顺序
print(A.__subclasses__()) #查看类的子类

print("*"*100)
print()

#浅拷贝和深拷贝_对象内存分析
    #浅拷贝: 只拷贝对象的引用，不拷贝对象的内容
    #深拷贝: 完全拷贝对象的内容
    #copy: 浅拷贝
    #deepcopy: 深拷贝
    #copy和deepcopy的区别: copy是浅拷贝，deepcopy是深拷贝

import copy
class MobilePhone:
    def __init__(self,cpu):
        self.cpu = cpu

class CPU:
    pass

c = CPU()
m = MobilePhone(c)

print("浅拷贝")
m2 = copy.copy(m) #浅拷贝
print("m:",id(m))
print("m2:",id(m2))
print("m.cpu:",id(m.cpu))
print("m2.cpu:",id(m2.cpu))
print()
print("深拷贝。。。。")
m3 = copy.deepcopy(m) #深拷贝
print("m:",id(m))
print("m3:",id(m2))
print("m.cpu:",id(m.cpu))
print("m3.cpu:",id(m3.cpu))

print("*"*100)
print()

#继承和组合
    #继承: 子类继承父类的属性和方法
    #组合: 一个类的属性是另一个类的对象
    #继承和组合的区别: 继承是is-a的关系，组合是has-a的关系
    #继承和组合的选择: 优先选择组合，避免多重继承

class CPU:
    def calculate(self):
        print("正在计算，算123456！")

class Screen:
    def show(self):
        print("正在显示画面")

class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen

c = CPU()
s = Screen()
m = MobilePhone(c,s) #组合

m.cpu.calculate() #调用CPU的方法

print("*"*100)
print()

#设计模式_工厂模式实现

class Benz:pass
class BMW:pass
class BYD:pass

class CarFactory:
    def createCar(self,brand): # 根据品牌创建汽车
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()

factory = CarFactory()
c1 = factory.createCar("奔驰")
c2 = factory.createCar("宝马")
print(c1)
print(c2)

print("*"*100)
print()

#设计模式_单例模式实现
    #单例模式: 一个类只能创建一个对象
    #实现单例模式的方法: __new__方法、装饰器、模块
    #__new__方法: 创建对象时自动调用，返回对象的引用
    #装饰器: 通过装饰器实现单例模式
    #模块: Python的模块是天然的单例模式

class MySingleton:
    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs): #创建对象时自动调用
        if cls.__obj == None: #判断对象是否为空
            cls.__obj = object.__new__(cls) #创建对象
        return cls.__obj #返回对象的引用

    def __init__(self,name):
        if MySingleton.__init_flag:
            print("初始化第一个对象。。。")
            self.name = name
            MySingleton.__init_flag = False #初始化第一个对象


a = MySingleton("aa")
print(a)
b = MySingleton("bb")
print(b)

print("*"*100)
print()

#设计模式_工厂和单例模式结合起来
class AllCar:
    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs): #创建对象时自动调用
        if cls.__obj == None: #判断对象是否为空
            cls.__obj = object.__new__(cls) #创建对象
        return cls.__obj #返回对象的引用

    def __init__(self):
        if AllCar.__init_flag:
            self.factory = CarFactory()
            AllCar.__init_flag = False

    def createCar(self,brand):
        return self.factory.createCar(brand)

a = AllCar()
b = AllCar()
print(a)
print(b)
print(a.createCar("奔驰"))
print(b.createCar("宝马"))

















