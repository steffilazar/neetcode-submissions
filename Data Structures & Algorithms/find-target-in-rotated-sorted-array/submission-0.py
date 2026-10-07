class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums)-1
        result=-1

        while l<=r:

            m=l+(r-l)//2

            if nums[m]==target:
                result= m
            elif nums[l]<nums[m] and nums[l]<target<nums[m]:
                r=m-1
            else:
                l=m+1
        return result
            
        