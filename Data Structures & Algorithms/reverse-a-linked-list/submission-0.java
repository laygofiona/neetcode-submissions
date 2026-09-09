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
    public ListNode reverseList(ListNode head) {
        // create nodes curr, prev, nextTemp
        ListNode curr = new ListNode();
        ListNode prev = null;
        ListNode nextTemp = new ListNode();
        // traverse through the list
        curr = head;
        while(curr != null){
            // set nextTemp to be equal to the node after curr
            nextTemp = curr.next;
            // set current node's next pointer to point to prev node
            curr.next = prev;
            // make prev point to the current node
            prev = curr;
            // make curr point to its original next node
            curr = nextTemp;
        }

        // curr is now null at the end
        // prev is now pointing to the old last node
        return prev;

    }
}