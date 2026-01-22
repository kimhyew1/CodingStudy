# heap에서의 min heap으로 가장 작은 숫자들을 제거하고 반환
# 그리고 그 다음 두번째로 작은 숫자들을 제거하고 반환 --> heappop으로 
# 섞은 음식의 스코빌지수를 계산해서, 해당 같을 리스트에 넣음. 

# 위의 3개를 반복하고, 중간에 횟수를 체크하는 것도 만들것. 
# 전부 K이상이 되는지 확인하고 그때 횟수를 반환하도록.
import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    heapq.heapify(scoville)
    lists = []

    for i in range(len(scoville)):
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + (second * 2)
        lists  = heapq.heappush(scoville, mixed)
        num = i

        if min(scoville) < K :
            if len(scoville) != 0:
                num += 1
                continue
            else: 
                return -1
        else:
            return (num + 1)
    

# 정확성: 67.7  효율성: 0.0 
# 사용자가 작성한 코드는 몇 가지 문제점이 있어서 예상대로 동작하지 않을 수 있습니다. 
# 우선, 힙을 통해 최소 두 개의 스코빌 지수를 꺼내고 새로운 스코빌 지수를 만들어서 다시 힙에 추가하는 흐름은 잘 구현하셨습니다. 
# 하지만 `num` 변수를 사용하는 로직에서 문제가 발생합니다.
# 1. `num` 변수의 값이 매 반복마다 증가하게 되어, 결과적으로 정말 섞은 횟수를 제대로 세지 못할 수 있습니다. 
# 최소한 두 개의 음식을 섞는 경우에만 카운트를 증가시켜야 합니다.
# 2. `if min(scoville) < K:` 조건으로 스코빌 지수를 항상 검사하고 있지만, 처음 두 개의 항목을 꺼내기 전에 확인하면 에러가 발생할 수 있습니다. 
# 이렇게 하면 스코빌 지수가 K에 도달하지 않는 경우에 적절히 처리되지 않을 수 있습니다.
# 3. `heapq.heappush()`의 결과로 `lists`에 값을 할당하는 부분은 필요하지 않습니다. 
# 메소드는 `None`을 반환하므로 잘못된 동작을 발생시킵니다.
# 이를 바탕으로, 올바르게 작동하도록 코드를 점검하고 수정해보세요. 
# 주의 깊게 변수를 관리하고 힙의 상태를 잘 모니터링 하는 것이 중요합니다.

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)

    for i in range(len(scoville)):
        num = i

        if scoville[0] < K :
            if len(scoville) != 0:
                first = heapq.heappop(scoville)
                second = heapq.heappop(scoville)
                mixed = first + (second * 2)
                heapq.heappush(scoville, mixed)
                num += 1
                
            else: 
                return -1
        else:
            return num 
        

# 정확성: 71.0 효율성: 16.1
# 1. **종료 조건**: 현재 코드는 `for` 루프를 사용하여 `scoville`의 길이만큼 반복하고 있습니다. 
# 하지만, 음식을 섞는 과정에서는 스코빌 지수가 K보다 작은 동안 계속해서 섞어야 하므로, 실제로는 `while` 루프를 사용하는 것이 적절합니다. --> while 조건을 바꿔!
# 이로 인해 음식을 섞지 않는 경우에도 반복이 계속될 수 있습니다.
# 2. **최솟값 체크**: `scoville`의 길이가 0이 될 경우를 체크하고 있으나, 스코빌 지수가 K 이상이 되었는지 체크하는 논리가 부족합니다. 
# 현재는 스코빌 지수가 K 이상일 때 반환하도록 설정되어 있는데, 실제 섞기 작업 이후에 다시 스코빌 지수를 체크해야 합니다.
# 3. **횟수 계산**: 섞은 횟수를 세는 변수를 잘못 설정하고 있습니다. 
# `num` 변수를 루프 내부에서 증가시키는데, 이로 인해 제대로 된 횟수를 반환하지 않을 수 있습니다. 
# 섞일 때마다 카운트하는 로직이 필요합니다.
# 이런 문제들을 해결하기 위해, `while` 반복문을 사용하고, 조건문을 적절히 수정해보세요. 각 단계에서 확인이 필요하도록 코드를 재구성해 보세요.

import heapq 

def solution(scoville, K):
    heapq.heapify(scoville)
    i = 0

    while scoville[0] < K:
        if len(scoville) >= 2:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            mixed = first + (second * 2)
            heapq.heappush(scoville, mixed)
            i += 1
        else :
            return -1
    else :
        return i

print(solution(scoville, K))
                
