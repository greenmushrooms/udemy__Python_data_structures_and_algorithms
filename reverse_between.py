class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
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
        duration = self.length
        i = 1 
        while i <= duration :
            print(temp.value)
            temp = temp.next  
            i += 1  
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between (self, pos1, pos2):
        current = self.head 
        l = self.length
        next = current.next
        i = 1 
        while i < pos1:
            previous = current
            current = next 
            next = current.next 
            i += 1
        
        pre_head = previous
        head = current 
        i += 1 


        print(f"starting loop at possition {i}")
        while i <= pos2 : 
            current.next = previous 

            previous = current 
            current = next
            next = current.next 

            print(f"previous is {previous.value}, current is {current.value}, i is {i}" )
            i += 1 
            

        current.next = previous 
        head.next = next 
        pre_head.next = current 

        

        
        


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.print_list()
linked_list.reverse_between(2,4)
linked_list.print_list()
# print("Original linked list: ")
# linked_list.print_list()

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
