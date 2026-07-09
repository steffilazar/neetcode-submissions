class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        
        count=0
        longest=0

        for x in num:
            if x-1 in num:
                count=0
            
            while x+count in num:
                count+=1
            longest=max(count,longest)
        
        return longest