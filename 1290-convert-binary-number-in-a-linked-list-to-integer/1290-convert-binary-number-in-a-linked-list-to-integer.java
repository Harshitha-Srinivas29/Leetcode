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
    public int getDecimalValue(ListNode head) {
        ListNode node = head;
        String s = "";
        while(node != null){
            s += Integer.toString(node.val);
            node = node.next;
        }
        int ans = Integer.parseInt(s, 2);
        return ans;
    }
}