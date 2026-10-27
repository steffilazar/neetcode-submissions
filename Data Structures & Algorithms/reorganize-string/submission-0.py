class Solution:
    def reorganizeString(self, s: str) -> str:
        
        count=Counter(s)
        maxheap=[[-c,char] for char,c in count.items()]
        heapq.heapify(maxheap)

        prev=None
        res=""

        while prev or maxheap:

            if prev and not maxheap:
                return ""

            c,char=heapq.heappop(maxheap)
            res+=char
            c+=1

            if prev:
                heapq.heappush(maxheap,prev)
                prev=None
            if c!=0:
                prev=[c,char]
        return res


