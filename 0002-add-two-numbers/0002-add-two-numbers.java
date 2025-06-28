/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    ListNode result = new ListNode(0);
    ListNode head = result;
    int carry = 0;

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
         if (l1 == null && l2 == null && carry == 0) return null;

        int sum = l1.val + l2.val + carry;
        carry = sum / 10;
        result.next = new ListNode(sum % 10);
        result = result.next;

        if(l1.next != null && l2.next != null)
            addTwoNumbers(l1.next, l2.next);
        else if(l1.next != null)
            addTwoNumbers(l1.next, new ListNode(0));
        else if(l2.next != null)
            addTwoNumbers(new ListNode(0), l2.next);
        else if(carry > 0){
            result.next = new ListNode(1);
            result = result.next;
        }

        return head.next;
    }
}