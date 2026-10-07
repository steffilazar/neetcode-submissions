class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        
        l=1
        r=max(piles)
        safe=h
        result=r

        while l<=r:
            m=l+(r-l)//2
            h=safe
            for i in piles:
                rem=i

                while rem>0:
                    rem=rem-m
                    h-=1
                    
            
            if h<= 0:
                l=m+1
            elif h> 0:
                result=m
                r=m-1
            
        return result
