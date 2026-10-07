class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r=max(weights)
        l=0

        while True:
            cap=r
            ships=1
            for w in weights:
                if cap-w<0:
                    ships+=1
                    cap=r

                cap-=w
            
            if ships<=days:
                return r
            
            r+=1