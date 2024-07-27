class Node: 
    def __init__(self, value) -> None:
        self.value = value 
        self.next = None 
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node 
        self.length = 1
    
    def print_list(self):
        current = self.head 
        while current is not None: 
            print(current.value)
            current = current.next


my_dll = DoublyLinkedList(7)
my_dll.print_list()