class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m=len(nums1)
        n=len(nums2)
        l1=0
        l2=0
        arr=[0]*(m+n)
        i=0

        while l1<m and l2<n:
           
            if nums1[l1]<=nums2[l2]:
                arr[i]=nums1[l1]
                l1+=1
                i+=1
            else:
                arr[i]=nums2[l2]
                l2+=1
                i+=1
            
        l,r=0,len(arr)-1

        m=l+(r-l)//2

        if len(arr)%2==0:
            return (arr[m]+arr[m+1])/2
        else:
            return float(arr[m])

        
                

