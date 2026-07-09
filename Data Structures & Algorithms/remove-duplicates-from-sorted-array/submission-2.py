class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l=1
        n=len(nums)

        for r in range(1,len(nums)):
            if r<n and nums[r]!=nums[r-1]:
                
                nums[l]=nums[r]
                l+=1
                
            r+=1

        return l
        