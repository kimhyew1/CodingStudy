# 우선 시작은 무조건 (으로만 가능 --> 문자열에서 첫 글자(기호) 어떻게 뽑는지
# (와 )의 쌍이 같아야함. --> 문자열에서 중복 개수 세는 법
# 2가지 조건을 모두 만족할떄 True, 그 외에의 경우는 False

s = "()()"

def solution(s):
    first_string = '('
    if (first_string == s[0]) and (s.count('(') == s.count(')')):
        answer = True
    else :
        answer = False
    return answer



# ()) 이렇게 닫힘이 더 많은 경우도 고려해야함. --> 즉, 순서도 고려!
# ( 일때 숫자가 올라가고, )일떄 숫자가 줄어들면서 음수이면 False
# 처음부터 )이면 음수니까 Flase가 맞음. 그리고 쌍이 안맞아도 중간 어디서 아님 끝에서 False --> 위에서의 조건을 모두 만족

def solution(s):
    count = 0
    for nums in s:
        if nums == "(":
            count += 1
        else:
            count -= 1
            if count < 0 :
                answer = False
                return answer  #여기서 return을 해야지 코드가 끝남!!

    if count == 0:
        answer = True
    else :
        answer = False

    return answer       