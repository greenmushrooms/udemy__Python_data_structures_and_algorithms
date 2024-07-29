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

    def append(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node 
        else:
            self.tail.next = new_node 
            new_node.prev = self.tail 
        self.tail = new_node 
        self.length += 1 
        return True 
    
    def pop(self):
        if self.length == 0: 
            return None 
        
        temp = self.tail 

        if self.length == 1: 
            self.tail = None 
            self.head = None 
        else: 
            self.tail = self.tail.prev      
            self.tail.next = None 
            temp.prev = None 
        
        self.length -= 1

        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0: 
            self.tail = new_node 
        else:     
            self.head.prev = new_node
            new_node.next = self.head 

        self.head = new_node 
        self.length += 1
        return True 
    
    def pop_first(self):  
        if self.length == 0:
            return None 
        temp = self.head 
        if self.length ==1: 
            self.head = None 
            self.tail = None
        else:
            self.head = self.head.next 
            self.head.prev = None 
            temp.next = None 

        self.length -= 1 
        return temp
    
    def get(self,index):
        if self.length < index or index < 0: 
            return None 
        

        if index < self.length/2:
            temp = self.head 
            for _ in range(index):
                temp = temp.next
        else: 
            temp = self.tail 
            for _ in range(self.length -1,index, -1):
                temp = temp.prev
        
        return temp

    def set(self,index,value):

        temp = self.get(index)
        if temp: 
            temp.value = value 
            return True
        return False 

    def insert(self, index, value):
        if self.length < index or index < 0: 
            return None 
        if index == 0: 
            self.prepend(value)
        if index == self.length:
            self.append(value)
        
        new_node = Node(value)
        
        temp = self.get(index)
        temp_next = temp.next
        temp.next = new_node 
        temp_next.prev = new_node
        new_node.prev = temp
        new_node.next = temp_next 

        return True 


        



my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)
my_dll.print_list()
print("-------")
my_dll.set_value(1,6)
my_dll.print_list()

