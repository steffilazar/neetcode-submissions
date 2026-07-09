class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxx=0

        while l<r:
            if heights[l]<heights[r]:
                vol=heights[l]*(r-l)
                l+=1
                if vol>maxx:
                    maxx=vol
            else:
                heights[l]>heights[r]
                vol=heights[r]*(r-l)
                r-=1
                if vol>maxx:
                    maxx=vol
        return maxx

            

        