## 완주하지 못한 선수

# 순서대로 정렬한 후에 달라지는 주소값을 반환하고자 함!
# if - else 문을 사용하여 answer = 현재의 return 값으로 받아오는 것이 기존 코드였지만, 현재의 return 값을 두개받을 수 있도록 수정했음.
# 효율성이 좋아졌음

def solution(participant, completion):

    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):      
        
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(completion)] 

