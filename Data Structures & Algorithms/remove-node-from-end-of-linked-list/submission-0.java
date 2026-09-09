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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Figure out how many nodes are in the linkedlist
        int list_length = 0;

        ListNode counter = head;

        while(counter != null){
            // Increment list_length
            list_length++;
            // Move on to the next node
            counter = counter.next;
        }

        // if number of nodes is equal to n
        if(list_length == n){
            // then set new head to be the next node after head
            head = head.next;
        } else {
            // create a variable called p which is the length of the linked list
            int p = list_length;

            // create curr and prev pointers
            ListNode prev = new ListNode(0, head);
            ListNode curr = head;

            // go through the linkedlist from the head
            while(curr != null){
                // check if n is equal to p
                if(n == p){
                    // found the node to remove
                    prev.next = curr.next;
                    break;
                } 

                // decrease counter p
                p--;
                prev = prev.next;
                curr = curr.next;
            }
        }

        return head;
    }
}
