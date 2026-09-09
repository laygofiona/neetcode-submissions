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
    public boolean hasCycle(ListNode head) {
        // Define two pointers, fast and slow
        // They both start at the head
        ListNode fast = head;
        ListNode slow = head;

        // Go through the linked list while neither fast and fast.next pointers are null
        while(fast != null && fast.next != null){
            // keep moving fast by 2 nodes
            fast = fast.next.next;
            // keep moving slow by 1 node
            slow = slow.next;

            // check if fast and slow pointers are at the same node
            if(fast == slow){
                // there is a cycle
                return true;
            }
            
        }

        // if this line is reached then there is no list
        return false;
    }
}
