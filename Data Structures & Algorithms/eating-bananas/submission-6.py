
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        
        l=1
        r=max(piles)
        safe=h
        result=r
        

        while l<=r:
            m=l+(r-l)//2
            hrs=0
            for i in piles:
                hrs+= math.ceil(i/m)
            if hrs> h:
                l=m+1
            else:
                
                r=m-1
                result=m
                
        return result
            