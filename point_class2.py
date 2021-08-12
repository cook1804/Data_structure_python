#<Point 클래스의 메쏘드 (연산자 오버로딩 포함)>

"""메쏘드에는 __init__,__str__,__len__ 등과 같이 magic method라 불리는 특별한 메쏘드와 일반 메쏘드로 구분할 수 있다
magic method의 이름은 두 개의 underscore로 메쏘드 이름을 감싼 형태이다.
"""

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return Point(self.x - other.x, self.y - other.y)

    def __rmul__(self,other):
        return Point(self.x * other, self.y * other)

"""def add(self, other):
       return Point(self.x + other.x, self.y + other.y)
p = Point(1,2)
q = Point(3,4)
r = p.add(q)
print(r)    # r = (4,6)"""

"""이렇게 생성할수도 있지만, 정수, 실수 덧셈처럼 r = p + q 의 형식으로 + 연산자를 사용할 수 있다면 직관적이라 이해하기 쉬운 장점이 있다. 
파이썬에서는 이를 위한 magic 메쏘드를 제공한다. 정수, 실수의 덧셈 연산자에 Point클래스의 덧셈 연산을 '덧 입혔다'는 의미에서 이러한 기능을
'연산자 overloading'이라 한다"""

"""특별 메쏘드의 이름은 __add__ 이다. r = p + q를 하면, 실제로는 r = p.__add__(q)가 호출되어,
두 벡터의 합 벡터가 리턴되어 r에 저장된다."""

p = Point(1,2)
q = Point(3,4)
r = p + q
s = p.__add__(q)
a = p - q
b = p.__sub__(q)
print(r,s)
print(a,b)

"""이제 곱셈 연산을 생각해보자. 두 벡터의 곱은 덧셈이나 뺄셈처럼 대응되는 좌표 값을 더하거나 빼는 식으로 
정의되지 않는다. 벡터의 곱셈 연산은 r = 3 * p의 형태처럼 p의 좌표 값에 모두 상수 3을 곱하는 식으로 사용된다.
즉, scalar * vector 형식으로 사용된다."""

"""scalar 값은 Point 객체가 아니기 때문에 연산에 참여하는 두 객체의 타입이 같지 않다는 문제가 발생한다. 
파이썬에서는 이러한 경우에도 연산자 오버로딩 기능을 지원한다. 단, 오른쪽 객체를 기준으로 오버로딩을 해야한다.
__rmul__(right multiplication)magic 메쏘드는 * 연산자의 오른쪽에 등장하는 객체가 self가 되고 
왼쪽 객체가 other가 되는 형식이다. 그래서 이름에 r이 붙었다. 이 경우에 self와 other의 타입이 달라도 된다."""
# r = 3 * p    # r = p.__mul__(3)의 형식으로 호출됨(반대가 아님에 유의!)

r = 3 * p
print(r)
r = p * 3    # 이 문장은 에러를 발생시킨다. self가 오른쪽에 와야함!
print(r)