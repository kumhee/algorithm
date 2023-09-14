class Stack:
    def __init__(self):
        # 스택을 초기화하는 생성자 메서드
        # 스택은 비어있는 리스트로 초기화
        self.stack = []
        
    def __len__(self):
        return len(self.stack)
        
    def is_empty(self):
        # 스택이 비어있는지 여부를 확인하는 메서드
        # 스택이 비어있으면 True를 반환하고, 그렇지 않으면 False를 반환
        return len(self.stack) == 0
    
    def push(self, item):
        # 스택에 새로운 요소를 추가하는 메서드
        # 주어진 요소를 스택의 맨 위에 추가합니다.
        self.stack.append(item)
        
    def pop(self):
        # 스택에서 요소를 제거하고 반환하는 메서드
        if self.is_empty():
            return "Empty" # 스택이 비어있으면 "Empty" 문자열을 반환
        else :
            return self.stack.pop() # 스택이 비어있지 않으면 스택의 맨 위 요소를 제거하고 반환
            
    def peek(self):
        if self.is_empty():
            return "Empty"
        else :
            return self.stack[-1]
        
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.is_empty())
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.is_empty())


print("")
print("문제------------------------------")
print("")
# 문제 : 괄호 짝 맞추기
# (), {}, [] 짝이 맞는지
# () : true
# ()[]{} : true
# {] : false
# ([)] : false

def is_valid(a):
    stack = Stack()
    open = "([{"
    close = "}])"
    
    for char in a:
        if char in open:
            stack.push(char)
        elif char in close:
            if len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if(char == ')' and top != '(') or \
                    (char == ']' and top != '[') or \
                    (char == '}' and top != '{'):
                    return False
                
    return len(stack) == 0
            
print(is_valid('()')) #true
print(is_valid('{(})')) #false
print(is_valid('((()))')) #true
print(is_valid('(((({]}))))')) #false
print(is_valid('()[]{}')) #true