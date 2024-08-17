class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def is_palindrome(self):
        left_node = self.head 
        right_node = self.tail
        for _ in range(round(self.length-1 /2) ):
            if left_node.value != right_node.value:
                return False 
            left_node = left_node.next 
            right_node = right_node.prev 
        return True 





# my_dll_1 = DoublyLinkedList(1)
# my_dll_1.append(2)
# my_dll_1.append(3)
# my_dll_1.append(2)
# my_dll_1.append(1)

# print('my_dll_1 is_palindrome:')
# print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print(my_dll_2.length)
print(my_dll_2.is_palindrome)
print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )
print(my_dll_2.length)
my_dll_2.append(3)
my_dll_2.length
print( my_dll_2.is_palindrome() )


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

"""

