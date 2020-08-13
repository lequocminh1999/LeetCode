#https://leetcode.com/problems/student-attendance-record-i/

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=0
        for i in range(0,len(s)):
            if s[i]=='L' and i>1:
                if s[i-1]=='L' and s[i-2]=='L':
                    return False
            if s[i]=='A':
                a=a+1
                if a>1:
                    return False
        return True
            