class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def insertion_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    sorted_head = None
    current = head

    while current is not None:
        next_node = current.next
        sorted_head = insert_node_sorted(sorted_head, current)
        current = next_node

    return sorted_head


def insert_node_sorted(sorted_head, new_node):
    if sorted_head is None or new_node.data < sorted_head.data:
        new_node.next = sorted_head
        return new_node

    current = sorted_head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return sorted_head


def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


list1 = Node(3)
list1.next = Node(7)
list1.next.next = Node(10)

list2 = Node(1)
list2.next = Node(5)
list2.next.next = Node(8)


print("Original List 1:")
print_linked_list(list1)

print("\nOriginal List 2:")
print_linked_list(list2)


reversed_list1 = reverse_linked_list(list1)
print("\nReversed List 1:")
print_linked_list(reversed_list1)


sorted_list2 = insertion_sort_linked_list(list2)
print("\nSorted List 2:")
print_linked_list(sorted_list2)


def main():
    merged_list = merge_sorted_lists(reversed_list1, sorted_list2)
    print("\nMerged List:")
    print_linked_list(merged_list)


if __name__ == "__main__":
    main()
