def solution(A):
    for i in range(1, len(A) + 1):
        if i not in A:
            return 0

    return 1
