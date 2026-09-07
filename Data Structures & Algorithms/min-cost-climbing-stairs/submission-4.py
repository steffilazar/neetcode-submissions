class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0]*(n+1)
        dp[1],dp[0]=0,0

        for i in range(2,n+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[n]
        























       #bottom up
        n=len(cost)
        dp=[0]*(n+1)

        for i in range(2,n+1):
            dp[i]= min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
            
        return dp[n]

        prev, prev2=0,0

        for n in cost:
            temp=prev+ n
            prev=second
            second=temp
        return prev


