from typing import Optional

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Optional['Node'] = None
        self.prev: Optional['Node'] = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self, limit=10):
        output = []
        current_node = self.head
        count = 0
        while current_node is not None and count < limit:
            output.append(str(current_node.value))
            current_node = current_node.next
            count += 1
        print(" <-> ".join(output))

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        current = self.head

        if not current or not current.next:
            return

        self.head = current.next

        while current and current.next:
            first_node = current
            second_node = current.next

            first_node.next = second_node.next
            second_node.prev = first_node.prev

            if first_node.next:
                first_node.next.prev = first_node

            if second_node.prev:
                second_node.prev.next = second_node
            else:
                self.head = second_node

            second_node.next = first_node
            first_node.prev = second_node

            current = first_node.next






my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

print('my_dll after swap_pairs:')
my_dll.swap_pairs()
my_dll.print_list()




"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""
