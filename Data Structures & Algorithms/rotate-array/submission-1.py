class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        b=[0]*n
        k=k%n
        for i in range(n):
            b[(k+i)%n]= nums[i]
            
        
        for i in range(n):
            nums[i]=b[i]


