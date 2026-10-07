class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        b=[0]*n
        l=0
        r=l+k
        while r < n:
            b[l]=nums[r]
            l+=1
            r+=1
        r=0
        while r<k:
            b[l]=nums[r]
            l+=1
            r+=1
        for i in range(n):
            nums[i]=b[i]


