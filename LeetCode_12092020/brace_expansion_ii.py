# https://leetcode.com/problems/brace-expansion-ii/

class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        def creation(s):
            res=set()
            if s=="": 
                res.add("")
                return res
            if s[0]!='{':
                lmao=creation(s[1:])
                for l in lmao:
                    #print(l)
                    res.add(s[0]+l)
            if s[0]=='{':
                cnt=0
                la=1
                for i in range(1,len(s)):
                    if s[i]=='{':
                        cnt+=1
                    if s[i]=='}':
                        if cnt!=0:
                            cnt-=1
                        else:
                            res.update(list(creation(s[la:i])))
                            ss=creation(s[i+1:])
                            result=set()
                            for ll in res:
                                for lll in ss:
                                    result.add(ll+lll)
                            return result
                    if s[i]==',' and cnt==0:
                        res.update(list(creation(s[la:i])))
                        la=i+1
            return res
        result=list(creation(expression))
        result.sort()
        return result