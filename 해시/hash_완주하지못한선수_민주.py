participant = ["mislav", "stanko", "mislav", "ana"] 
completion = ["stanko", "ana", "mislav"]

# 배열들을 딕셔너리로 바꿔야하지...
# key value : 이름 완주여부T/F
# 참가명단을 바꿔야..? 아니면 참가명단-completion으로 생각을 해야?
# 바꾸면 F남는 것을 반환하면 되는 것. 빼면 남는 것...어떻게 빼야하는지
# 같은 키가 존재하면 T로 바꾸기 가능 --> 동명이인은?


# 차잡합 개념으로 진행 
hash_comp = {}
for item in completion:
    hash_comp[item] = True

answer = []
for item in participant:
    if item not in hash_comp:
        answer.append(item)

print(answer) 

# -> 동명이인 조건 불만족.
# 'leo'로 나와야하는데 ['leo']로 나옴


# 동명이인을 만족해야함. -> 충돌 해결 전략 필요!
# 정렬해서, 각 이름의 개수를 새기
# key 개수가 다르면, 완주를 못한 다른 이름이 사람이 있는것. 
# key개수가 같은데 value에서 문제가 생기면, 완주를 못한 사람이 동명이인 
def solution(participant, completion):
    sort1 = sorted(participant)
    sort2 = sorted(completion)
    count1 = {}
    for name in sort1:
        count1[name] = count1.get(name, 0) + 1
    count2 = {}
    for name in sort2:
        count2[name] = count2.get(name, 0) + 1
       
    answer = ''

    if count1 != count2: 
        keys = set(count1.keys()) - set(count2.keys())
        answer = keys
    else: 
        values = set(count1.values()) - set(count2.values())
        answer = values

    answer = list(answer)[0]
    return answer

## >> IndexError: list index out of range
## >> 테스트 결과 (~˘▾˘)~  3개 중 2개 성공
# 검색한 결과 counter를 사용해서 해결. 
print(participant)
print(completion)
diff = Counter(participant) - Counter(completion)
print(diff)


from collections import Counter

def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    return list(diff.keys())[0]
solution(participant, completion)
