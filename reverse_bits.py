#https://leetcode.com/problems/reverse-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        val=0
        x=1
        a=[]
        for i in range(0,32):
            a.append(0)
        for i in range(0,32):
            if n%2==0: a[i]=0
            else: a[i]=1
            n=n/2
        for i in range(31,-1,-1):
            val=val+x*a[i]
            x=x*2
        return val
        
        