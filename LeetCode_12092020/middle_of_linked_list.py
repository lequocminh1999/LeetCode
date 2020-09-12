# https://leetcode.com/problems/middle-of-the-linked-list/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        si=0
        cur=head
        while cur:
            si=si+1
            cur=cur.next
        cnt=0
        cur=head
        print(si)
        while cur:
            print(cnt)
            cnt=cnt+1
            if (si/2)+1==cnt:
                return cur
            cur=cur.next
        