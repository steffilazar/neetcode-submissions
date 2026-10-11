class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        ans=float('inf')

        if nums[l]<nums[r]:
            return nums[l]
        
        if len(nums)==1:
            return nums[0]

        while l<r:
            m=(l+r)//2

            if nums[m]>nums[r]:
                l=m+1
            if nums[m]<nums[r]:
                r=m
                ans=min(ans,nums[m])
        return nums[l]
                
