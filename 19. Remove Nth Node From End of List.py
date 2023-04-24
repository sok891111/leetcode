# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        if length -n == 0:
            return head.next

        cur = head
        count = 0
        while cur:
            if count == length -n -1:
                tmp = cur.next
                cur.next =tmp.next
            cur = cur.next
            count += 1

        return head
