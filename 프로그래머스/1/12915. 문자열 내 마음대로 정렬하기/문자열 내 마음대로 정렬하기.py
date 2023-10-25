def solution(strings, n):
    # 해결 방식 
    # 1. 포문 돌려서 str[n] 번째를 dictionary 형태로 val, index 값 저장한다.
    # 2. 저장된 dic sort()
    #     arr = []
    #     for (str,i) in strings:
    #         arr.append(str[n], i)        
    #     arr.sort()
    
    # lamda란 ? 익명함수
    # def sum(a + b) { return a + b }
    # sum = lambda a, b: a + b
    
    # map, filter, sort 에서 장점 발휘
    # s1 = ['banana', 'kiwi', 'apple']
    # s4 = sorted(s1, key = lambda x : len(x), reverse = True)
    # print(s4)
    #['kiwi', 'apple', 'banana']
    
    strings.sort(key = lambda x : x[n] + x)

    return strings;