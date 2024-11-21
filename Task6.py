from collections import deque

user_input = input().split()
queue = deque()

def calculator(a:int, b:int, operator:str)-> int:
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a // b


for c in user_input:
    if c not in '*+-/':
        queue.append(int(c))
    else:
        while len(queue) > 1:
            num1 = queue.popleft()
            num2 = queue.popleft()
            queue.appendleft(calculator(num1, num2, c))
           
print(queue.popleft())