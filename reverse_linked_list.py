from LinkedList import SinglyLinkedList


def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    head = prev

    return head


def main():
    ll = SinglyLinkedList()
    for i in xrange(15):
        ll.append(i)

    rev = reverse_linked_list(ll.head)
    
    for i in reversed(xrange(15)):
        assert i == rev.val
        rev = rev.next


main() 
