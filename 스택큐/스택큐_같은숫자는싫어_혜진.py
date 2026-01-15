
def solution(arr):
    answer = [arr[0]] # 첫번째 원소는 포함해줌.
    
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]: # 원소값이 변화가 생기면 추가함.
            answer.append(arr[i])
    return answer