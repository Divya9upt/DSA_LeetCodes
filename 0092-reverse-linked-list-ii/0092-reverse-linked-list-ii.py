# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        # move prev to the node just before position `left`
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next  # this node ends up at the tail of the reversed section

        for _ in range(right - left):
            nxt = curr.next          # node to move to the front
            curr.next = nxt.next     # unlink it
            nxt.next = prev.next     # point it at the current front of the section
            prev.next = nxt          # make it the new front

        return dummy.next