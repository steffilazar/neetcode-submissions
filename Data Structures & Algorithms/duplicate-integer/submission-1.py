class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listt = list()
        for num in nums:
            if num in listt:
                return True
            listt.append(num)
        return False