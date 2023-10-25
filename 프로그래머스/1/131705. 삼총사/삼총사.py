def solution(number):
    
    # 해결방법
    # 1. list 요소 값을 삭제하면서 접근
    # 2. list 위치 값에 접근

    answer = 0

#     for idx, i in enumerate(number):
#         number.pop(0)
#         for jdx, j in enumerate(number):
#             number.pop(0)
#             for k in number:
#                 print(i, j, k)
#                 if i + j + k == 0:
#                     answer += 1
            
#     return answer

    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1

    return answer
