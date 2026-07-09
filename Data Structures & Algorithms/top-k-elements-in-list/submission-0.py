class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashh={}

        for num in nums:
            if num in hashh:
                hashh[num]+=1
            else:
                hashh[num]=1

        result=[]
        
        for x in range(k):
            freq=max(hashh,key=hashh.get)
            result.append(freq)
            del hashh[freq]

        return result
            
        
        


           
  

        