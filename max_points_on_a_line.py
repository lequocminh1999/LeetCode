#https://leetcode.com/problems/max-points-on-a-line/

import numpy as np
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res=0
        dict={}
        n=len(points)
        for i in range(0,n):
            noi=0
            for j in range(0,n):
                l=points[i]
                ll=points[j]
                if l==ll: noi+=1
                if l[0]==ll[0]: continue
                sl=np.float128((l[1]-ll[1]))/np.float128((l[0]-ll[0]))
                
                if sl not in dict: 
                    dict[sl]=1
                    res=max(res,dict[sl]+noi)
                else:
                    dict[sl]=dict[sl]+1
                    res=max(res,dict[sl]+noi)
            dict.clear()
            cal=0
            for j in range(0,n):
                ll=points[j]
                if j==i:
                    res=max(res,1)
                    continue
                if ll[0]==l[0]:
                    cal=cal+1
                    res=max(res,cal+1)
        
        return res