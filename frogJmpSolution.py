def solution(X, Y, D):
    jumps = 0

    while X < Y:
        X = X + D
        jumps += 1

    return jumps
