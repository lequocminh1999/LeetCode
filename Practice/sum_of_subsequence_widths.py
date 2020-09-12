#https://leetcode.com/problems/sum-of-subsequence-widths/

class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        n=int(n)
        pow2=list()
        modd=pow(10,9)+7

        A.sort()
        cur=1
        for i in range(0,n):
            pow2.append(cur)
            cur=(cur*2)%modd


        total=0
        for i in range(0,n):
            total=(total+pow2[i]*A[i])%modd
            total=(total-pow2[n-1-i]*A[i])%modd
        return total
        