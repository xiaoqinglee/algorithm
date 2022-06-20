package problems

import "github.com/xiaoqinglee/algorithm/pkg"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *pkg.ListNode) *pkg.ListNode {
	aLen, bLen := 0, 0
	for headANode := headA; headANode != nil; headANode = headANode.Next {
		aLen += 1
	}
	for headBNode := headB; headBNode != nil; headBNode = headBNode.Next {
		bLen += 1
	}
	if aLen > bLen {
		aLen, bLen = bLen, aLen
		headA, headB = headB, headA
	}

	//now a is shorter

	headANode := headA
	headBNode := headB
	for i := 1; i <= bLen-aLen; i += 1 {
		headBNode = headBNode.Next
	}
	for headANode != headBNode && headBNode != nil && headBNode != nil {
		headANode = headANode.Next
		headBNode = headBNode.Next
	}
	return headANode // 如果不相交最后 headANode headBNode 都是nil
}
