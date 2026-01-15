def solution(progresses, speeds):
    Days = []
    answer = []
    
    for i in range(len(progresses)):
        for j in range(1, 100):
            if progresses[i] + speeds[i] * j >= 100: # 작업에 속도의 배수를 곱해준 것이 100 이상이 되면 break 하고, days에 추가함
                break
        Days.append(j)
    
    counts = 1 # 첫번째 작업은 100만 넘으면 배포되기 때문에 1로 지정.
    
    for k in range(1, len(Days)):
        if Days[k] <= Days[k-1]: # 이전 작업과 다음 작업의 days를 비교해서 다음 작업의 일수가 더 작으면 counts 증가함
            counts += 1
            Days[k] = Days[k-1]
        else:
            answer.append(counts) 
            counts = 1
    
    answer.append(counts)
    return answer