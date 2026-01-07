def solution(nums):
    name = {}   # Key: name of the pokemon, Value: num. of the pokemon
    n_select = int(len(nums) / 2)   # Num. that i have to select

    for subject in nums:   # Count the pokemons' number
        if subject in name.keys():   # If there's already exist in dictionary
            name[subject] += 1  
        else:   # If there's NOT exist in dictionary
            name[subject] = 1

    n_pokemon = len(list(name.keys()))   # Num. of the pokemon (Duplication X)

    if n_pokemon >= n_select:
        answer = n_select
    else:
        answer = n_pokemon
    return(answer)

nums = [3, 3, 3, 2, 2, 2]
result = solution(nums)
result   # 2
