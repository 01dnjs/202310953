'''
def get_circumference(radius):
    result=2*3.14*radius
    return result
def get_circle_area(radius):
    result=3.14*radius**2
    return result
small=1
c=get_circumference(small)
a=get_circle_area(small)
big=10
print(f'반지름 {small}인 원의 둘레는 {c:.2f}이고, 넓이는 {a:.2f}이다.')
print(f'반지름 {big}인 원의 둘레는 {get_circumference(big):.2f}이고, ',end='')
print(f'넓이는 {get_circle_area(big):.2f}이다.')
''
class Circle:
    def getCircumference(self):
        result=2*3.14159265*self.radius
        return result
    def getArea(self):
        result=3.14159265*self.radius**2
        return result
small=Circle()
big=Circle()
small.radius=1
big.radius=10
print(f'반지름 {small.radius}인 원의 ',end='')
print(f'둘레는 {small.getCircumference():.2f}이고, ',end='')
print(f'넓이는 {small.getArea():.2f}이다.')
print(f'반지름 {big.radius}인 원의 ',end='')
print(f'둘레는 {big.getCircumference():.2f}이고, ',end='')
print(f'넓이는 {big.getArea():.2f}이다.')
''
class Circle:
    def __init__(self,radius):
        self.__radius=radius
    def getCircumference(self):
        result=2*3.14159265*self.__radius
        return result
    def getArea(self):
        result=3.14159265*self.__radius**2
        return result
    def setRadius(self,radius):
        self.__radius=radius
    def getRadius(self):
        return self.__radius
big=Circle(10)
big.setRadius(100)
print(big.getRadius())
''
class Circle:
    __PI=3.14159265
    def __init__(self,radius):
        self.__radius=radius
    def getCircumference(self):
        result=2*Circle.__PI*self.__radius
        return result
    def getArea(self):
        result=Circle.__PI*self.__radius**2
        return result
small=Circle(1)
big=Circle(10)
''
class Circle:
    __PI=3.14159265
    @staticmethod
    def getPI():
        return Circle.__PI
print(Circle.getPI())
''
#11.1
class Point:
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y
    def show(self):
        print(f'({self.__x},{self.__y})')
    def set(self,x,y):
        self.__x=x
        self.__y=y
    def get(self):
        return (self.__x,self.__y)
def test():
    p1 = Point()
    p2 = Point(2, 3)
    p1.show(); print()
    p1.set(10, 20); p1.show(); print()
    p2.show(); print()
    x, y = p2.get()
    print(f'x={x}, y={y}')

if __name__ == '__main__':
    test()
''
#11.2
class Time:
    def __init__(self,h=0,m=0):
        self.__h=h
        self.__m=m
    def set(self,h,m):
        self.__h=h
        self.__m=m
    def display(self):
        print(f'{self.__h:02d}:{self.__m:02d}')
    def add(self,time):
        t=Time()
        hour=self.__h+time.__h
        minute=self.__m+time.__m
        if minute>=60:
            hour+=1
            minute-=60
        t.set(hour,minute)
        return t
    @staticmethod
    def is_valid(h,m):
        if 0<=h<=23 and 0<=m<=59:
            return True
        else:
            return False
def main():
    t1 = Time(9)
    t2 = Time(9, 30)
    t1.display()
    t2.display()
    later = t1.add(Time(1, 15))
    later.display()
    if Time.is_valid(25, 0):
        print('유효한 시각')
    else:
        print('유효하지 않은 시각')
if __name__ == '__main__':
    main()
'''
class Point:
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y
class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2
    def show(self):
        print(f'좌측 상단 꼭지점이 ({self.__x1},{self.__y1})이고 ',end='')
        print(f'우측 하단 꼭지점이 ({self.__x2},{self.__y2})인 사각형입니다.',end='')
    def getWidth(self):
        width=self.__x2-self.__x1
        return width
    def getHeight(self):
        height=self.__y2-self.__y1
        return height
    def getArea(self):
        w=self.getWidth()
        h=self.getHeight()
        area=w*h
        return area
    def getPerimeter(self):
        w=self.getWidth()
        h=self.getHeight()
        perimeter=2*(w+h)
        return perimeter
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
    
        
