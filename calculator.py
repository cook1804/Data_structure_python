"""infix 수식을 postfix 수식으로 바꾼 뒤 계산기를 만들어보자.
   피연산자는 그대로 outstack이라는 리스트에 넣고 연산자는 opstack이라는 스택 객체를 활용한다.
   고려해야 하는것은 예를 들어 input으로 (3+1)*4 를 받았을때, '(',')','+','*' 를 우선순위를 정하고 난뒤, 
   stack에서 우선순위가 높은것이 있을때와, 낮은것이 있을때 어떻게 작동해야하는지 고민해야 한다."""

# 먼저 stack을 사용하기때문에 Stack 기능을 하는 class를 만들어준다. 
class Stack:
    def __init__(self):
        self.item = []

    def push(self,val):
        self.item.append(val)

    def pop(self):
        try:
            return self.item.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.item[-1]
        except IndexError:
            print("Stack is empty")
        
    def __len__(self):
        return len(self.item)

# input 으로 infix 수식을 주면 output으로 postfix 수식을 출력하도록 프로그램을 짜본다. 

outstack = []    #postfix 수식을 저장할 공간.
opstack = Stack() # infix -> postfix 으로 바꾸기 위해 연산자들을 저장하는 공간.


input = '(3+1)*4'
