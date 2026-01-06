def solution(participant, completion) :
    check = {}   # Key: participant's name, Value: num. of participants
    for subject in participant:   # Count participant's frequency  (O(N))
        if subject in check:    # Already in dictionay (= Count namesake)
            tmp = check[subject]
            check[subject] = tmp + 1
        else:
            check[subject] = 1

    for subject in completion:   # Delete completion's frequency  (O(N))
        tmp = check[subject]
        check[subject] = tmp - 1

    tmp_idx = list(check.values()).index(1)   # Always "n(participant) - n(completion) = 1" holds  (O(N))
    answer = list(check.keys())[tmp_idx]
    return(answer)

participant = ["leo", "kiki", "eden", "eden"]
completion = ["eden", "kiki", "leo"]
answer = solution(participant, completion)
answer   # "eden"

# --------- Efficiency failed ---------
# def solution(participant, completion):   O(N^2)
#     answer = participant.copy()

#     for subject in completion:   O(N)
#         if answer.count(subject) != 0:
#             idx = [answer.index(subject)][0]   O(N)  
#             answer.pop(idx)  
#     return(','.join(answer))
