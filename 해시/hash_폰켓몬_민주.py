# 최대 종류를 아는 것 -> 중복을 없애면 된다. 

nums = [3,1,2,3]

def solution(nums):
    answer = len(set(nums))
    return answer
# 70점짜리 답변 
# -> 중복된 타입은 제거되지만, 선택할 수 있는 포켓몬의 개수인 N/2를 고려하지 않음. 


# N/2이거나, 아니면 중복 없앤 것 둘 중에서 min을 골라야 함. 
nums = [3,1,2,3]

def solution(nums):
    answer = 0
    first = len(nums) / 2 
    second = len(set(nums))
    answer = min(first, second)
    return answer
