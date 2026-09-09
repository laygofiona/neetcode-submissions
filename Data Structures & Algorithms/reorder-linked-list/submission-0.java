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
    public void reorderList(ListNode head) {
        // Find the middle of the list

        ListNode fast = head;
        ListNode slow = head;

        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        // slow pointer is at the middle of the list
        // split the list
        ListNode l2 = slow.next;
        slow.next = null;
        ListNode l1 = head;

        // Reverse the second half of the list
        ListNode prev = null;
        ListNode curr = l2;
        ListNode tmpCurr = null;

        while(curr != null){
            tmpCurr = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmpCurr;
        }


        // merge the second half with the first half
        ListNode second = prev;
        ListNode first = head;
        // go through the nodes of the first half
        while(second != null){
            ListNode tmpl1 = first.next;
            ListNode tmpl2 = second.next;
            first.next = second;
            second.next = tmpl1;
            first = tmpl1;
            second = tmpl2;
        }
        
        
    }
}
