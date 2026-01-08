## 폰켓몬

# num의 길이를 먼저 구하고, num을 정렬하였음.
# 앞뒤로 비교해서 달라지는 주소값을 count에 모으고
# count의 길이와 N/2의 길이를 비교해서 정답을 구함

def solution(nums):
    answer = 0
    
    N = len(nums)
    nums.sort()
    
    count = []

    for i in range(N-1):
        if nums[i] != nums[i+1]:
            count.append(i)
    if len(count) < N/2:
        answer = len(count)+1
    else:
        answer = N/2
        
    return answer