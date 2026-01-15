def solution(s):
    answer = True
    
    l = ")" # 시각적으로 보기 편하려고, l, r로 지정함.
    r = "("
    
    if s.count(l) != s.count(r): # 괄호의 개수가 다르면 false 반환
        return False
    
    if s[0] == ")": # 닫는 괄호로 시작하면 false 반환
        return False
    
    count = 0 # 완성된 괄호 쌍의 개수
    for ch in s: 
        if ch == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    
    return True
