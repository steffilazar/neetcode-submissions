class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1

        while l<=r:
            m=l+(r-l)//2

            if target==nums[m]:
                return True

            if nums[l]<nums[m]:
                if target<nums[l] or target>nums[m]:
                    l=m+1
                else:
                    r=m-1
                
            elif nums[l]>nums[m]:
                if target>nums[r] or target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                
                l += 1
        return False