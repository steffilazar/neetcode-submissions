class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-1 -(k-1)]

        nums=[-n for n in nums]

        heapq.heapify(nums)
        l=0
        while l<k:
            cur=heapq.heappop(nums)
            l+=1
        return -cur