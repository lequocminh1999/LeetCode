#https://leetcode.com/problems/sum-of-distances-in-tree/

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        e=list()
        par=list()
        ssub=list()
        noc=list()
        res=list()
        for i in range(0,N):
            d=list()
            e.append(d)
            nn=0
            par.append(-1)
            ssub.append(nn)
            noc.append(nn)
            if i<N: res.append(nn)
        
        for i in edges:
            u= i[0]
            v= i[1]
            e[u].append(v)
            e[v].append(u)
        
        def spread(v):
            for i in e[v]:
               if par[i]==-1:
                par[i]=v
                (x,y)=spread(i)
                ssub[v]=ssub[v]+x+y+1
                noc[v]=noc[v]+y+1
            return (ssub[v],noc[v])
        
        
        def cal(v):
            if v==0: res[v]=ssub[v]
            else: res[v]=res[par[v]]+N-2*noc[v]-2
            for i in e[v]:
                if par[i]==v:
                    cal(i)
               
        par[0]=0
        spread(0)
        cal(0)
        return res
        