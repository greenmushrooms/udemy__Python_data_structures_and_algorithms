from typing import Optional

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Optional['Node'] = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        l = self.length
        i = 0
        while temp is not None and i <= l+1:
            print(temp.value)
            temp = temp.next
            i+=1

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between (self, pos1, pos2):
        if pos1 == pos2:
            return None

        current = self.head
        previous = current
        next = current.next

        i = 0
        #lining up with the start
        while i < pos1:
            previous = current
            current = next
            next = current.next
            i += 1

        print(f"reversing list at {current.value}")

        pre_head = previous
        head = current

        print(f"pre_head is {pre_head.value}, head is {head.value}")

        #reversing the block
        while i < pos2  :
            #move up 1

            previous = current
            current = next
            next = current.next

            if next != None:
                print(f"previous is {previous.value} , current is {current.value},next is {next.value}")
            else:
                print(f"previous is {previous.value} , current is {current.value},next is None")
            i += 1
            #reverse link
            current.next = previous



        # print(f"pre_head is {pre_head.value}, head is {head.value}, next is {next.value}")
        #setting the block in list
        if pos1 == 0:
            self.head = current
        else:
            pre_head.next = current

        # print(f"pre_head is {pre_head.value if pre_head != None else 'None' }, head is {head.value}, next is {next.value if next != None else 'None'}")
        # head.next = next
        if next != None:
            head.next = next
        else:
            head.next = None
        # else



linked_list = LinkedList(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

print("Original linked list: ")
linked_list.print_list()

print("reverse entire list")
linked_list.reverse_between(1,4)
linked_list.print_list()
# # Reverse a sublist within the linked listd
# linked_list.reverse_between(2, 4)
# print("Reversed sublist (2, 4): ")
# linked_list.print_list()

# # Reverse another sublist within the linked list
# linked_list.reverse_between(0, 4)
# print("Reversed entire linked list: ")
# linked_list.print_list()

# # Reverse a sublist of length 1 within the linked list
# linked_list.reverse_between(3, 3)
# print("Reversed sublist of length 1 (3, 3): ")
# linked_list.print_list()

# # Reverse an empty linked list
# empty_list = LinkedList(0)
# empty_list.make_empty
# empty_list.reverse_between(0, 0)
# print("Reversed empty linked list: ")
# empty_list.print_list()


# """
#     EXPECTED OUTPUT:
#     ----------------
#     Original linked list:
#     1
#     2
#     3
#     4
#     5
#     Reversed sublist (2, 4):
#     1
#     2
#     5
#     4
#     3
#     Reversed entire linked list:
#     3
#     4
#     5
#     2
#     1
#     Reversed sublist of length 1 (3, 3):
#     3
#     4
#     5
#     2
#     1
#     Reversed empty linked list:
#     None

# """
