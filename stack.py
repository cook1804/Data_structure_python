class Stack:
    def __init__(self):   #생성함수. self라는 객체를 나타내는 매개변수로 전부 시작해야한다.
        self.items = []   # 멤버변수의 이름. 쉽게말해 리스트의 이름을 items로 정함. 원하는 이름으로 변경해도 상관없다.
    
    def push(self,val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    
    def __len__(self):         # 만일 print(len(S)) 가 실행되면 __len__(self) 함수를 호출하게 되고, __len__ 은 len(self.items)를 불러 return 한다.
        return len(self.items) # len이 단위 시간 O(1)인것은 항상 len의 값을 저장하고 있기 때문에 불러 오기만 하면 되므로 O(1)이다.

# Stack 은 모든 함수(메서드)가 O(1) 시간이다. 
"""__len__()은 카운터로 작동하며 데이터가 정의되고 저장되면 자동적으로 증가한다.
결과적으로 인터프리터에게 순회하며 길이를 가져오라는 명령대신 이미 저장된 value를 가져오게 된다.
이렇게 len()은 O(1)의 시간 복잡도를 가지게 되었다."""
