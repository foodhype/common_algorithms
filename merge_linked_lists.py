from LinkedList import SinglyLinkedList


def merge_linked_lists(a, b):
    head = None
    temp = None

    if a is not None and b is not None:
        if a.val < b.val:
            temp = a
            a = a.next
        else:
            temp = b
            b = b.next  
        head = temp

    while a is not None and b is not None:
        if a.val < b.val:
            temp.next = a
            a = a.next
        else:
            temp.next = b
            b = b.next        
        temp = temp.next

    if a is not None:
        temp.next = a
    if b is not None:
        temp.next = b

    return head


def merge_linked_lists_r(a, b):
    if a is None:
        return b
    if b is None:
        return a

    if a.val < b.val:
        a.next = merge_linked_lists(a.next, b)
        return a
    else:
        b.next = merge_linked_lists(a, b.next)
        return b


def main():
    ll1 = SinglyLinkedList()
    ll2 = SinglyLinkedList()
    for i in xrange(8):
        ll1.append(i)
    for i in [-1, 0, 2, 7, 8, 9]:
        ll2.append(i)

    merged_ll_head = merge_linked_lists(ll1.head, ll2.head)

    expected = [-1, 0, 0, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9]
    for num in expected:
        assert num == merged_ll_head.val
        merged_ll_head = merged_ll_head.next

    ll3 = SinglyLinkedList()
    ll4 = SinglyLinkedList()
    for i in xrange(8):
        ll3.append(i)
    for i in [-1, 0, 2, 7, 8, 9]:
        ll4.append(i)

    merged_ll_head = merge_linked_lists_r(ll3.head, ll4.head)

    expected = [-1, 0, 0, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9]
    for num in expected:
        assert num == merged_ll_head.val
        merged_ll_head = merged_ll_head.next


if __name__ == "__main__":
    main()
