class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        listt=list()

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target:
                    listt.append(i)
                    listt.append(j)
                    return listt
                
