def solution(A):
    for i in A:
        if A.count(i) % 2 != 0:
            return i
