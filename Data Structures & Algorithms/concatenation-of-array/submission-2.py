class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n=len(nums)
        num=[0] * 2*n
       

        for i, x in enumerate(nums):
            num[i]=num[i+n]=x

        return num

        