class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for x,y in points:
            dist= (y*y+x*x)
            minheap.append([dist,x,y])
        heapq.heapify(minheap)
        res=[]
        while len(res)<k:
            cur=heapq.heappop(minheap)
            res.append(cur[1:3])
        return res