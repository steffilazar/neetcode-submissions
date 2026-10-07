class Solution:
    def search(self, nums: List[int], target: int) -> int:


            l=0
            r=len(nums)-1
            result=1001

            while l<=r:
                
                m=l+(r-l)//2

                if nums[m]==target:
                    return m
                if nums[l]<=nums[m]:
                    target<nums[m] and target<=nums[l] or target>nums[m]
                    l=m+1
                else:
                    r=m-1
            return -1
            
                



            
        