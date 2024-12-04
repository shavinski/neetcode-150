# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# loop through different nodes
# keep count of visited nodes
# or maybe a set?
# can add to set if it is not in
# if the node is already in set, then return false
#


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        cur = head

        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next

        return False
