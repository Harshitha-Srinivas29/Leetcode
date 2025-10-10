import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        head = tail = ListNode(0)
        
        # Build initial heap
        for num in lists:
            if num:
                heapq.heappush(h, (num.val, id(num), num))
        
        while h:
            _, _, node = heapq.heappop(h)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(h, (node.next.val, id(node.next), node.next))
        
        return head.next
