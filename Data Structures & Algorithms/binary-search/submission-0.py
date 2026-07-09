class Solution:
    def search(self, nums: List[int], target: int) -> int:

            mid=len(nums)//2

       
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                for i in range(mid,len(nums)):
                    if target==nums[i]:
                        return i 
            else:
                for i in range(0,mid):
                    if target==nums[i]:
                        return i 
            return -1

        