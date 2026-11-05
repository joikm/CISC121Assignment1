def solution(A):
    # check each number from 1 to N+1
    for i in range(1, len(A) + 2):
        # if number is missing from array return missing number
        if i not in A:
            return i
