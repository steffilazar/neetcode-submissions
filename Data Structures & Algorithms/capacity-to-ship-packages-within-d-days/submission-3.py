class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l=max(weights)
        r=sum(weights)
        res=r

        def canship(mid):
            capacity=mid
            ship=1
            for i in weights:
                if capacity-i<0:
                    ship+=1
                    capacity=mid
                    if ship>days:
                        return False

                capacity-=i
            return True

        while l<=r:
            mid=l+(r-l)//2

            if canship(mid):
                r=mid-1
                res=min(res,mid)

            else:
                l=mid+1
            
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