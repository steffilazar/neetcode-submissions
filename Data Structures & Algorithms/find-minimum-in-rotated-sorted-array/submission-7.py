class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l=0
        r=len(nums)-1
        result=1001

        while l<=r:
            if nums[l]<nums[r]:
                result= min(result,nums[l])
                
                
            m=l+(r-l)//2
            result= min(result,nums[m])

            if nums[l]<=nums[m]:
                l=m+1
            else:
                r=m-1
        return result