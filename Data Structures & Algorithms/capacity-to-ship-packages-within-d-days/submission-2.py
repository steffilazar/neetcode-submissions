class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r=sum(weights)
        l=max(weights)
        result=r

        def canShip(m):
            ships=1
            cap=m

            for w in weights:
                if cap-w<0:
                    ships+=1
                    cap=m
                    if ships>days:
                        return False
                    
                cap-=w
            return True

        while l<=r:
            m=l+(r-l)//2

            if canShip(m):
                result=min(result,m)
                r=m-1
            else:
                l=m+1
        return result