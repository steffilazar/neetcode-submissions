class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r

        while l<=r:
            mid=l+(r-l)//2
            hrs=0
            for pile in piles:
                hrs+=math.ceil(pile/mid)
          
            if hrs<=h:
                r=mid-1
                res=mid
                
            else:
                l=mid+1

        return res