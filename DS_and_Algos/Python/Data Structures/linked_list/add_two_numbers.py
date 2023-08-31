# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # just add the numbers and reverse the result, it is the same
        carry = 0
        dummy = ListNode()
        cur = dummy
        
        while l1 or l2 or carry:

           v1 = l1.val if l1 else 0
           v2 = l2.val if l2 else 0

           res = v1 + v2 + carry
           carry = res // 10
           res = res % 10

           cur.next = ListNode(res)

           cur = cur.next
           l1 = l1.next if l1 else None
           l2 = l2.next if l2 else None
        
        return dummy.next

