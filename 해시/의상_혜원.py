def solution(clothes):
    closet = {}   # Key: cloth's type, Value: cloth's name
    for info in clothes:   # Count num. of cloth 
        clothes_type = info[1]
        if clothes_type in closet.keys():   # If cloth already exist
            closet[clothes_type] += 1
        else:
            closet[clothes_type] = 1

    answer = 1
    n_clothes = list(closet.values())   # Make into list w. only cloth's num.
    for i in range(0, len(n_clothes)):   # Combination of the clothes
        answer = answer * (n_clothes[i] + 1)

    return answer-1   # Subtract the case that have nothing to wear

clothes = [["yellow_hat", "headgear"], 
           ["blue_sunglasses", "eyewear"], 
           ["green_turban", "headgear"]] 
answer = solution(clothes)
answer   # 5
