# bottom up
def solution1(X):
    def a(x):
        return x*5
    def b(x):
        return x*3
    def c(x):
        return x*2
    def d(x):
        return x+1

# top down
def solution2(X):
    def a(x):
        return x//5
    def b(x):
        return x//3
    def c(x):
        return x//2
    def d(x):
        return x-1
    dp = [0]*(X+1)
    dp[1] = 1
    for i in range(1, X):
        if X % 5==0:
            dp[i] = dp[i//5]+1
        elif X % 3==0:
            dp[i] = dp[i//3]+1
        elif X % 2==0:
            dp[i] = dp[i//2]+1
        else:
            dp[i] = dp[i-1]+1
    return dp[X]

    