def solution(numbers):
    sum = 0
    for number in numbers:
        sum += number
          
    answer = 0
    answer = sum / len(numbers)
    return answer