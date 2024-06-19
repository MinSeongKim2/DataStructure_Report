# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    stack = []
    result = 0
    for char in input:
        if char == '(':
           stack.append(char) 
        else: 
           if stack: 
            stack.pop() 
           else: 
            result += 1 # +1

    for char in input:
        print(char)

    result += len(stack)
    return result

    
result = problem2(input)

assert result == 3
print("정답입니다.")


