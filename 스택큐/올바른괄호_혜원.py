def solution(string):
    if string.startswith(")"):    # 빠르게 끝내려고 예외처리 
        return False 

    n = len(string)
    if n % 2 != 0:    # 빠르게 끝내려고 예외처리 
        return False

    l = list(string)   # 전체 문자열을 리스트로 형 변환 
    l_cnt = r_cnt = 0    # l_cnt: "(" 개수, r_cnt = ")" 개수 

    for i in range(n):
        if l[i] == "(":
            l_cnt += 1
        elif l[i] == ")":
            r_cnt += 1
        if l_cnt - r_cnt < 0:    # 제대로 닫히지 않은채 전개되면 강제 종료 
            return False
    
    if l_cnt == r_cnt:
        return True
    else:
        return False
