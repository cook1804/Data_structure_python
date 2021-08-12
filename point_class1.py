"""Point 클래스는 2차원 평면의 점 (또는 2차원 벡터)을 나타내는 클래스이다. 
* 필요한 멤버는 점의 x-좌표와 y-좌표이다."""

class Point:
    def __init__(self, x=0, y=0):
        self.x = x  # x-좌표를 위한 멤버 self.x
        self.y = y  # y-좌표를 위한 멤버 self.y

    def __str__(self):
        return f"({self.x},{self.y})"   # 문자열 출력

    #생성함수(magic method 중 하나)__init__의 매개변수로 두 좌표 값을 받는다. default 좌표값은 0으로 정했다.(다른 default 값으로 지정해도 상관없다.)
    #클래스의 모든 메쏘드의 첫 번째 매개변수는 이 메쏘드를 호출하는 객체를 나타내는 self이어야 한다. 


# p = Point(1,2)
# print(p)   # <__main__.Point object at 0x10976f910>
"""print(p)를 수행하면 객체 p를 프린트해야하는데, 구체적으로 어떤 내용을 출력해야 하는지 print 함수는 전혀 알지 못한다
print 함수에게 어떤 내용을 출력해야 하는지 알려줘야 한다. 그 역할을 하는 magic method가 __str__함수이다.
print(p)의 실행과정은 (1) p가 속한 클래스의 Point의 __str__ 함수가 정의되어 있다면 호출한다.
이 __str__함수는 출력용 문자열을 리턴하는 데, print 함수는 단순히 리턴된 문자열을 출력하는 역할이다.
만약, (2) __str__ 함수가 정의되어 있지 않다면, 해당 객체의 기본 정보(<__main__.Point object at 0x10976f910>)를 출력한다."""




