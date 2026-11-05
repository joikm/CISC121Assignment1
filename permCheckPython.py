def solution(A):
    # check each number from 1 to N
    for i in range(1, len(A) + 1):
        if i not in A: # if a number is missing, its not a permutation
            return 0
    return 1 # return 1 if all numbers are present
