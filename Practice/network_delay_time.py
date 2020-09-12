#https://leetcode.com/problems/network-delay-time/

import heapq

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        edge=[]
        c=[]
        for i in range(0,N+1):
            l=[]
            edge.append(l)
            c.append(pow(10,9)+7)
        for l in times:
            u=l[0]
            v=l[1]
            w=l[2]
            edge[u].append((v,w))
        c[K]=1
        pq=[]
        heapq.heapify(pq)
        heapq.heappush(pq,K)
        while pq:
            u=heapq.heappop(pq)
            for (v,w) in edge[u]:
                alt=c[u]+w
                if alt < c[v]:
                    c[v]=alt
                    heapq.heappush(pq,v)
        ma=1
        for i in range(1,N+1):
            if c[i]==(pow(10,9)+7): return -1
            ma=max(ma,c[i])
        return ma-1
        
            
        