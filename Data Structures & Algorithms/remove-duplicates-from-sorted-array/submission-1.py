class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        stop=set(nums)
        stop=sorted(list(stop))

        for i in range(len(stop)):
            nums[i]=stop[i]
        return len(stop)

        