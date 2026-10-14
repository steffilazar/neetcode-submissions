class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque()
        time=0
  

        for i in range(len(tickets)):
            q.append(i)

        while q:
            time+=1
            i=q.popleft()
            tickets[i]-=1
            if tickets[i]==0:
                if i==k:
                    return time
                   
            else: 
                q.append(i)
            
        return time
