class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res=[]
        path=[]
        remaining=target

        def bt(i,remaining):
            if remaining==0:
                res.append(path[:])
                return
            if remaining<0 or i==(len(nums)):
                return
            
            for i in range(i,len(nums)):
                path.append(nums[i])
                bt(i,remaining-nums[i])
                path.pop()
        bt(0,target)
        return res

        # res=[]
        # path=[]
        # remaining=target

        # def bt(i,remaining):

        #     if remaining==0:
        #         res.append(path[:])
        #         return

        #     if remaining<0 or i==len(nums):
        #         return
            
        #     path.append(nums[i])
        #     bt(i,remaining-nums[i])
        #     path.pop()

        #     bt(i+1,remaining)

                 
        # bt(0,remaining)
        # return res