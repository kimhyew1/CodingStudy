def solution(arr):
    answer = list()
    n = len(arr)

    answer.append(arr[0])
    for i in range(1, n):   # O(N)
        target = arr[i]
        if target != answer[-1]:   # Compare with the last elements
            answer.append(target)
  return answer

arr = [1,1,3,3,0,1,1]
answer = solution(arr)
answer   # [1,3,0,1]
