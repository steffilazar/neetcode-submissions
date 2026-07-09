class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        summ=0
        minn = float('inf')

        for r in range(len(nums)):
            summ+=nums[r]

            while summ>=target:
                
                summ-=nums[l]
                minn=min(minn,r-l+1)
                l+=1
                

        return 0 if minn == float('inf') else minn