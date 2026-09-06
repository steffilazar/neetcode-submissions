class Solution:
    def climbStairs(self, n: int) -> int:
        memo={0:1, 1:1}

        def fi(x):
            if x in memo:
                return memo[x]
            else:
                memo[x]=fi(x-2)+fi(x-1)
                return memo[x]
        return fi(n)