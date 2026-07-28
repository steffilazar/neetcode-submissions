class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k= m+n-1
        i, j= m-1, n-1

        while j>=0:
            if i>=0 and nums1[i]>=nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1



        # s=[]
        # n1,n2=0,0
        # b=[0]*(m+n)
        # i=0
        # while n1 <m and n2<n:
        #     if nums1[n1]<nums2[n2]:
        #         b[i]=nums1[n1]
        #         n1+=1
        #     else:
        #         b[i]=nums2[n2]
        #         n2+=1
        #     i+=1
        # while n1<m:
        #     b[i]=nums1[n1]
        #     n1+=1
        #     i+=1
        # while n2<n:
        #     b[i]=nums2[n2]
        #     n2+=1
        #     i+=1

        # for i in range(m+n):
        #     nums1[i]=b[i]

