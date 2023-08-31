def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
	dummy = ListNode(None, head)
	prev, cur = dummy, head

	while cur and cur.next:
		prev.next = cur.next
		cur.next = cur.next.next
		prev.next.next = cur
		prev, cur = cur, cur.next
	return dummy.next

# [1, 2, 3, 5, 9]
# dummy = [0, next - null]
# prev = dummy
# cur = [1, [next - 2]]
# then, prev = [0, 1, ]
# 
