# Point 클래스를 Vector 클래스로 확장

#Vector 클래스 설계
"""Point 클래스는 2차원의 점 또는 2차원 벡터만을 위한 클래스이므로, 
3차원, 4차원 등의 여러 차원 벡터를 자유롭게 표현할 수 있는 Vector 클래스가 필요하다
__init__에 전달하는 초기 좌표 값의 개수는 벡터의 차원에 따라 결정되므로 매개 변수의 개수를 마음대로 지정할 수 있는 기능을 사용한다.
def function(*args): 라고 함수를 정의하면, 임의의 개수를 매개 변수들을 tuple args를 통해 전달할 수 있다. """


"""_coords처럼 _ 하나로 시작하는 멤버 변수는 nonpublic 변수로 만약 이 클래스를 다른 곳에서 import해
사용하는 경우에는 nonpublic 멤버는 import 되지 않고 감춰진다. 좌표 값을 참조하기 위해선, magic 메쏘드
__getitem__과 __setitem__을 사용한다. """
class Vector:
    def __init__(self, *args):
        self._coords = list(args) #[x for x in args]

    def __str__(self):
        return str(self._coords)

    def __len__(self):  # return its dimension
        return len(self._coords)
    
    def __getitem__(self, k): # return the value of kth dimension
        return self._coords[k]
    
    def __setitem__(self, k, val): # return the value of kth dimension
        self._coords[k] = val

v = Vector(1,2,3)
v[-1] = 9

for c in v:
    print(c, end=" ")
print()