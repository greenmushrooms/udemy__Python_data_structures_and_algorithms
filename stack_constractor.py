from typing import Optional

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Optional['Node'] = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height > 0:
            new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None

        temp = self.top
        if self.height > 1:
            self.top = temp.next
        temp = None
        self.height -= 1

my_stack = Stack(1)
my_stack.push(2)

my_stack.print_stack()
my_stack.pop()

my_stack.print_stack()
