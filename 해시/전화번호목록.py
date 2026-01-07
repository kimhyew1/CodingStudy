def solution(phone_book):
    answer = True   # Initial value
    phone_book.sort()   # Sort ("12","1235","123" > "12","123","1235")  O(N logN)

    n = len(phone_book)   # Num. of the list's element
    for i in range(0, n-1):   # O(N)
        m = len(phone_book[i]) 
        if phone_book[i] in phone_book[i+1][:m]:   # Only compare the 1st~mth part 
            answer = False   # If condition satisfied
            break

    return answer

phone_book = ["119", "97674223", "1195524421"]
answer = solution(phone_book)
answer   # False
