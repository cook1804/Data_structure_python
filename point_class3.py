# Point 클래스 메쏘드 - 일반 

"""연산자 오버로딩을 통한 산술 연산을 구현하는 것 이외에 필요한 연산은 점 길이(벡터의 길이), 내적, 외적, 
두 점 사이의 거리, 점의 이동, 점의 회전 등 다양하다. 필요한 내용을 메쏘드로 구현하면 된다."""

import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def dot(self,q):
        return self.x*q.x + self.y*q.y
    
    def dist(self, q):
        return (self-q).length()

    def move(self, dx = 0, dy = 0):
        self.x += dx
        self.y += dy

p = Point(1,2)
q = Point(2,3)
print(f"p = {p}, q = {q}")
print("length of p =", p.length())
print("dot of p and q =", p.dot(q))
print("dist of p and q =", p.dist(q))
p.move(3,5)
print("move p by (3,5) =", p)