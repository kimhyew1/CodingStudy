# Heap (우선순위큐) -----------------------------------------------------
## 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조, 데이터를 우선순위에 따라 처리하고 싶을 때 사용
## 단순히 리스트를 이용해서 구현할수도, 혹은 heap을 이용해서 구현가능
## heap : 완전 이진 트리 자료구조의 일종으로, 항상 root node를 제거하는 것임.
## min heap : 루트 노드가 가장 작은 값, 값이 작은 데이터가 우선적으로 제거
## max heap : 루트 노드가 가장 큰 값, 값이 큰 데이터가 우선적으로 제거
#-----------------------------------------------------------------------
# stack: 가장 나중에 삽입된 데이터
# queue: 가정 먼저 삽입된 데이터
# priority queue: 가장 우선 순위가 높은 데이터
#-----------------------------------------------------------------------
import heapq


# 1) heapq.heappush(heap, item) : heap리스트에 item을 추가햐여 가장 작은 값의 index가 0이 되도록
heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
print(heap)


# 2) heapq.heappop(heap) : heap리스트에서 가장 작은 항목을 제거하고 반환함. 비어있으면 error
smallest = heapq.heappop(heap)
print(smallest)  
print(heap) 


# 3) heapq.heapify(list): list구조를 heap구조로 변환시킴.
data = [5, 1, 9, 3]
heapq.heapify(data)
print(data) 


# 4) 부호를 반대로 한다면 max heap 구현가능
data = [5, 1, 9, 3]
max_heap = []
for item in data:
    heapq.heappush(max_heap, -item) # 음수로 삽입
print(max_heap)

# 꺼낼 때 다시 부호를 바꿈
max_val = -heapq.heappop(max_heap)
print(max_val)  # 9


# 5) heap sort : 모든 요소를 힙에 넣은 뒤 하나씩 heappop을 한다면 오름차순으로 정렬된 결과를 얻을 수 있음
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))