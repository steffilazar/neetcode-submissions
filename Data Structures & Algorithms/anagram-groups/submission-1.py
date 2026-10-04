class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        

        for word in strs:
            seen=[0]*26

            for letter in word:
                seen[ord(letter)-ord('a')]+=1
            res[tuple(seen)].append(word)
        return list(res.values())
                

            


