#괄호 맞추기 
#(())() -> True
#())()(()) -> False

"""왼쪽 괄호는 자기 짝인 오른쪽 괄호가 올때까지 기다려야한다. 왼쪽 괄호를 Stack에 저장하여 짝이 맞는
   오른쪽 괄호가 나올때까지 저장해둔다."""

# 1. Stack 객체를 사용해야 하므로 Stack 클래스를 만든다.

class Stack:
    # 생성 함수
    def __init__(self):
        self.li = []
    
    # Stack에 val 추가 함수
    def push(self, val):
        self.li.append(val)

    # Stack의 맨 위에 있는 val 삭제하는 함수
    def pop(self):
        try:
            return self.li.pop()
        except IndexError:
            print("Stack is empty")
    # Stack의 맨 위에 있는 val    
    def top(self):
        try:
            return self.li[-1]
        except IndexError:
            print("Stack is empty")
    # Stack에 저장되어 있는 원소의 개수
    def __len__(self):
        return len(self.li) 

# 2. 괄호 맞추기 코드 작성. 

"""2-1. 우리는 왼쪽 괄호를 Stack에 저장하기로 하였으므로 Stack 객체 생성한다."""

S = Stack()
# brackets = input()   #입력 
brackets = '())()(())' #예시
for b in brackets:
    if b == '(':
        S.push()
    elif b == ')':
        if S.len() != 0:
            S.pop()
        else:
            print(False) #왼쪽 짝이 없이 오른쪽이 더 많은 경우 error
    else:
        print("input data Error") # '(',')' 이외의 값이 있을경우 error
if S.len() > 0:
    print("Error")  # for문을 다 끝내고 난 뒤, Stack의 len이 0 이상이면 '('가 더 많은 경우
else:
    print('True')   # 그 이외의 경우는 True
    
