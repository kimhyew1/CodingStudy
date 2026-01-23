import heapq

def solution(scoville, K):
    heapq.heapify(scoville)   # list >> heap
    cnt = 0   # initialise

    while scoville[0] < K:   # 전체가 K 이상인지 확인
        if len(scoville) < 2:   # 더 맵게를 진행할 수 없는 경우
             return -1
        
        target1 = heapq.heappop(scoville)
        target2 = heapq.heappop(scoville)

        new_scoville = target1 + 2*target2  
        heapq.heappush(scoville, new_scoville)   # insert new scoville
        cnt += 1

    return cnt

scoville = [2, 1, 3, 9, 12, 10]
K = 7
solution(scoville, K)   # 2
