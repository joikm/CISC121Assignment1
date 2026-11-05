def solution(A, K):
    if len(A) == 0:
        return A # return the array if it is empty

    # rotate array K times
    for i in range(K):
        last = A[-1] # get last element
        A = [last] + A[:-1] # move last element to front

    return A # return rotated array
