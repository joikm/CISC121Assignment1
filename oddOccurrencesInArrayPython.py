def solution(A):
    for i in A: # go through each number in array
        if A.count(i) % 2 != 0: # check if the number appears odd number of times
            return i # return unpaired number
