# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    mean = sum(input) // len(input)
    sorted_input = sorted(input)
    median = sorted_input[len(sorted_input) // 2]
    
    return [mean, median]

    mean = 0
    median = 0
    result = [0,0]
    
    result[0] = mean
    result[1] = median
    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")
