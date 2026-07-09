class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        num=[]

        
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            num.append(nums[i])
        
        for i in range(len(num)):
            nums[i]=num[i]
                
        return len(num)
        