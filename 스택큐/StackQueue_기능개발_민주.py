# 첫 배포에 순서대로 100이상인 것의 개수 (이때, 100미만이 있으면  stop)
# 다시 그 다음 배포에 순서대로 100이상인 것의 개수 ("")
# 각각 100이 되는 일수를 세고, 나오는 리스트로 끊기?
# 100이 되려면 100-prog에서 speed로 나누고, 소수점이 남을때 다 올려야.
# 두 리스트 순회하는 법을 알아야. 
# num2를 기준으로 이거보다 더 크면 새 묶음, 작거나 같으면 같은 묶음으로 
# 같은 묶음이라는 거는 갯수가 결국 늘어나는 것. 
# 추가적으로 반복이 끝나서 마지막 묶음도 저장해야함!

progresses = [93, 30, 55]
speeds = [1, 30, 5]

import math
def solution(progresses, speeds):
    days = []
    for i, j in zip(progresses, speeds) :
        day_count = math.ceil((100- i) / j)
        days.append(day_count)

    num2 = days[0]
    count = 1  # 0부터 하면 결과가 안나옴.
    count_list = []

    for num1 in days[1:]:
        if num1 <= num2:
            count += 1
        else: # 여기에서 이전에 만들어진 묶음을 저장해야.
            count_list.append(count)
            num2 = num1 
            count = 1
    count_list.append(count)
    return count_list


print(solution(progresses, speeds))