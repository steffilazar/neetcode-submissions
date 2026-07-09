class Solution:
    def search(self, nums: List[int], target: int) -> int:


            l=0
            r=len(nums)-1
            result=1001

            while l<=r:
                
                m=l+(r-l)//2

                if nums[m]==target:
                    return m
                    #left sorted
                if nums[l]<=nums[m]:
                    if target<nums[m] and target<nums[l] or target> nums[m]:
                        l=m+1
                    else:
                        r=m-1
                else:
                    if target>nums[m] and target>nums[r] or target<nums[m]:
                        r=m-1

                    else:
                        l=m+1
            return -1
            
                



            
        