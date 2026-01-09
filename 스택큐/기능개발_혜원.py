def solution(progresses, speeds):
    answers = list()

    while len(progresses) != 0:   # O(N)
        tmp = 0   # Cumulated days
        progresses = [p+s for p, s in zip(progresses, speeds)]    # If 1 day passed, how much works are progressed
        flags = list()   # DONE = T, NOT DONE = F

        for i in range(len(progresses)):   # O(N)
            flags.append(progresses[i] >= 100)

        while flags and flags[0]:   # O(N)
            tmp += 1
            progresses = progresses[1:]   # Pop the cumulated work
            speeds = speeds[1:]
            flags = flags[1:]
        answers.append(tmp)   # How many works are done in 1 day

    answers = [answer for answer in answers if answer != 0]
    return answers
