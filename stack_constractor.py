class Node: 
    def __init__(self, value) -> None:
        self.value = value 
        self.next = None 


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

my_stack = Stack(1)
my_stack.push(2)

my_stack.print_stack()