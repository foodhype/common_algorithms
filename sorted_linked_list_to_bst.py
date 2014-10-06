from BinaryTreeNode import BinaryTreeNode
from LinkedList import SinglyLinkedList
from binary_tree_traversal import inorder_traversal


def sorted_linked_list_to_bst(head):
    """Convert a sorted linked list to a binary search tree."""
    count = 0
    temp = head
    while temp is not None:
        temp = temp.next
        count += 1
    head_ref = [head] # tricky, tricky
    return sorted_linked_list_to_bst_helper(head_ref, count)


def sorted_linked_list_to_bst_helper(head_ref, n):
    if n <= 0:
        return None

    left = sorted_linked_list_to_bst_helper(head_ref, n // 2)

    root = BinaryTreeNode(head_ref[0].val)
    root.left = left

    head_ref[0] = head_ref[0].next

    root.right = sorted_linked_list_to_bst_helper(head_ref, n - (n // 2) - 1)

    return root


def main():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(1)
    ll.append(2)
    ll.append(5)
    ll.append(8)
    ll.append(8)
    ll.append(9)

    root = sorted_linked_list_to_bst(ll.head)

    expected = iter([1, 1, 2, 5, 8, 8, 9])
    
    for num in inorder_traversal(root):
        assert num == expected.next()


if __name__ == "__main__":
    main()
