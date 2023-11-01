def solution(id_list, reports, k):
    answer = []
    repoCheck = []
    reports = set(reports)
    
    for id in id_list:
        answer.append(0)
        #누구한테 몇번 신고를 당했는지 리스트
        repoCheck.append([[], 0])

    for report in reports:
        #list[0] : 신고한 사람
        #list[1] : 신고 당한 사람
        list = report.split(' ')
        
        #신고 당한 사람의 index -> repoCheck에 값 넣어줄거임
        reporter = id_list.index(list[0])
        repoIndex = id_list.index(list[1])

        repoCheck[repoIndex][0].append(reporter)
        repoCheck[repoIndex][1] += 1
        
        # if repoCheck[repoIndex][1] >= k:
        #     print("K번 이상")
        #     answer[police] +=1 
        #     print(answer)
    for rc in repoCheck:
        if rc[1] >= k:
            for index in rc[0]:
                answer[index] += 1
    return answer
