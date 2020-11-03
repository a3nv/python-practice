from leetcode.ListNode import ListNode


def insertionSortList(head: ListNode) -> ListNode:
    pseudo_head = ListNode()

    curr = head
    while curr:
        prev_node = pseudo_head
        next_node = prev_node.next
        while next_node:
            if curr.val < next_node.val:
                break
            prev_node = next_node
            next_node = next_node.next

        next_iter = curr.next

        curr.next = next_node
        prev_node.next = curr

        curr = next_iter

    return pseudo_head.next


if __name__ == "__main__":
    list = ListNode(4, ListNode(3, ListNode(5)))
    print(list)
    list = insertionSortList(list)
    print(list)
