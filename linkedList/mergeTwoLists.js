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
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     * [1, 2, 4], [1, 3, 5]
     * 
     * result = []
     * [1, 3], [2, 4] -> [1, 2, 3, 4]
     * list1 = 1, list 2 = 2
     * 
     *
     * mergeTwoLists(1, 2);
     *  list1.next = mergeTwoLists(3, 2) -> 2, 3, 4
     *  return list1.next -> 1, 2, 3, 4
     *
     * mergeTwoLists(3, 2);
     *  list2.next = mergeTwoLists(3, 4) -> 3 -> 4
     *  return list2 -> 2 -> 3 -> 4
     * 
     * mergeTwoLists(3, 4);
     *  list1.next = mergeTwoLists(null, 4) -> 4
     *  return list1 -> 3 -> 4
     * 
     * mergeTwoLists(null, 4);
     * !list1 return list2 (4)
     * 
     * 
     *   
     */

    mergeTwoLists(list1, list2) {
        if (!list1) return list2;
        if (!list2) return list1;

        if (list1.val <= list2.val) {
            list1.next = this.mergeTwoLists(list1.next, list2)
            return list1;
        } else {
            list2.next = this.mergeTwoLists(list1, list2.next);
            return list2;
        }
    }
}