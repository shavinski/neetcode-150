/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     * 
     * [0 -> 1 -> 2 -> 3] -> 
     * [0 <- 1 <- 2 <- 3]
     * 
     * neet to point 0 to null
     * but before need to hold the next value in temp variable to not cut connectoin
     * 
     * previous set to null at first
     * current node = head
     * 
     * 0 points to null
     * Null <- 0 
     * set current node to 
     * 
     */
    reverseList(head) {
        let prev = null;
        let current = head;

        while (current) {
            let temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }

        return prev;
    }
}