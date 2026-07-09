class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s=[]
        n1,n2=0,0
        b=[0]*(m+n)
        i=0
        while n1 <m and n2<n:
            if nums1[n1]<nums2[n2]:
                b[i]=nums1[n1]
                n1+=1
            else:
                b[i]=nums2[n2]
                n2+=1
            i+=1
        while n1<m:
            b[i]=nums1[n1]
            n1+=1
            i+=1
        while n2<n:
            b[i]=nums2[n2]
            n2+=1
            i+=1

        for i in range(m+n):
            nums1[i]=b[i]

