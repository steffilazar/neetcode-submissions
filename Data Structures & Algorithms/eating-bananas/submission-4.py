class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        safe = h
        result = r          # Bug 3 fix: safe default

        while l <= r:
            m = l + (r - l) // 2
            h = safe

            for i in piles:
                rem = i
                while rem > 0:
                    rem = rem - m
                    h -= 1

            if h >= 0:          # valid speed, try smaller
                result = m
                r = m - 1
            else:               # Bug 2 fix: elif → else
                l = m + 1

        return result