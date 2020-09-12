#https://leetcode.com/problems/unique-paths/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f=[]
        for i in range(0,m+1):
            l=[]
            for j in range(0,n+1): l.append(0)
            f.append(l)
        for i in range (1,m+1): f[i][1]=1
        for j in range (1,n+1): f[1][j]=1
        for i in range (2,m+1):
            for j in range (2,n+1):
                f[i][j]=f[i-1][j]+f[i][j-1]
        return f[m][n]
        