class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        first,second=0,0
        n=len(cost)

        for i in range(n-1):
            temp=max(first+cost[i],first+cost[i+1],second)
            first=second
            second=temp
        return temp -1