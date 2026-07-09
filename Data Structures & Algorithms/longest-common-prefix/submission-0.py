class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        shortest=min(strs,key=len)
        prefix=""

        for x in range(len(shortest)):
            check=shortest[x]
            for word in strs:
                if word[x]!=check:
                    return prefix
            prefix+=check

        return prefix


        