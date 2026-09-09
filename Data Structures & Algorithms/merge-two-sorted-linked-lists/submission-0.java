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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // go through nodes in list 1 and list 2 at the same time
        ListNode dummy = new ListNode();
        ListNode curr = dummy;
        while(list1 != null && list2 != null){
            if(list1.val < list2.val){
                curr.next = list1;
                list1 = list1.next;
            } else {
                curr.next = list2;
                list2 = list2.next;
            }
            // Go to the next node
            curr = curr.next;
        }


        // check for any remaining nodes in either l1 or l2
        if(list1 != null){
            // check if l1 still has more nodes
            curr.next = list1;
        } else if (list2 != null) {
            // check if l2 still has more nodes
            curr.next = list2;
        }


        return dummy.next;



    }
}