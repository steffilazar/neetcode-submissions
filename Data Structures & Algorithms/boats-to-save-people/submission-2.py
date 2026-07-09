class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        count = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1   # pair smallest with largest
                r -= 1
            else:
                r -= 1   # largest goes alone
            
            count += 1   # one boat used

        return count