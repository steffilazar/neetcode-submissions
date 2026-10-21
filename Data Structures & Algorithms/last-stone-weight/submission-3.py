class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # stones.sort()
        # n=len(stones)

        # if n==1:
        #     return stones[0]

        # for i in range(n):
        #     stones.sort()
        #     stones[n-2]=stones[n-1]-stones[n-2]
        #     stones[n-1]=0
        # return stones[n-2]

        stones=[-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            heapq.heappush(stones, first-second)
        stones.append(0)
        return abs(stones[0])
