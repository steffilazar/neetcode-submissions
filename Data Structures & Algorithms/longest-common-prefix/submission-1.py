class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        op=""
        shortest=min(strs)

        for i in range(len(shortest)):
            check=shortest[i]
            for word in strs:
                if word[i]!=check:
                    return op
            op+=check

        return op


            

        