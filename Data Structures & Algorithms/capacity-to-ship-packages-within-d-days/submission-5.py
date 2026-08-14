class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l=max(weights)
        res=r=sum(weights)


        def canship(mid):
            day=1
            cap=m
            for i in weights:
                if cap-i<0:
                    day+=1
                    cap=m
                cap-=i
            if day<=days:
                return True
            else:
                return False

        while l<=r:
            m=l+(r-l)//2

            if canship(m):
                r=m-1
                res=m
            else:
                l=m+1
        return res









        
                
















        # r=sum(weights)
        # l=max(weights)
        # result=r

        # def canShip(m):
        #     ships=1
        #     cap=m

        #     for w in weights:
        #         if cap-w<0:
        #             ships+=1
        #             cap=m
        #             if ships>days:
        #                 return False
                    
        #         cap-=w
        #     return True

        # while l<=r:
        #     m=l+(r-l)//2

        #     if canShip(m):
        #         result=min(result,m)
        #         r=m-1
        #     else:
        #         l=m+1
        # return result