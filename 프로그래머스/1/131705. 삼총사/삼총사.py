def solution(number):
    
    # 해결방법
    # 

    answer = 0

    for idx, i in enumerate(number):
        number.pop(0)
        for jdx, j in enumerate(number):
            number.pop(0)
            for k in number:
                print(i, j, k)
                if i + j + k == 0:
                    answer += 1
            
    return answer

