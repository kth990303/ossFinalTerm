import math

class Point:
    __x=0 # private 변수
    __y=0
    #생성자
    def __init__(self, x,y):
        self.x=x
        self.y=y
    #유클리디안 거리를 구하는 메소드
    def distance(self, self2):
        d=math.sqrt((self.x-self2.x)**2+(self.y-self2.y)**2)
        print(d)
    #두 점의 위치를 더하는 메소드
    def __add__(self, self2):
        x=self.x+self2.x
        y=self.y+self2.y
        print("(%d, %d)"%(x,y))

p1=Point(1,1)
p2=Point(2,2)
p1.distance(p2)
p1.__add__(p2)