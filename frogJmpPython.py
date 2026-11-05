def solution(X, Y, D):
    jumps = 0 # start with 0 jumps

    # keep jumping until the frog reaches the target
    while X < Y:
        X = X + D # move the frog forward
        jumps += 1 # add one to the jump count

    return jumps    # return total number of jumps

