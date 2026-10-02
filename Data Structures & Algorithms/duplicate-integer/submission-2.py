class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dup=set()

        for a in nums:
            if a in dup:
                return True
            else:
                dup.add(a)
        return False
        