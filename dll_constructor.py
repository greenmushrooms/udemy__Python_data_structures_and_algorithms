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

    def set_value(self,index,value):

        temp = self.get(index)
        if temp: 
            temp.value = value 
            return True
        return False 

    def insert(self, index, value):
        if self.length < index or index < 0: 
            return False 
        if index == 0: 
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)

        prev_node = self.get(index-1)
        next_node = prev_node.next 

        prev_node.next = new_node 
        next_node.prev = new_node 

        new_node.next = next_node 
        new_node.prev = prev_node 
        
        self.length += 1 
        return True 
    
    def remove(self, index ):
        if self.length < index or index < 0: 
            return None 
        if index == 0: 
            return self.pop_first
        if index == self.length:
            return self.pop
        

        temp = self.get(index)

        temp.next.prev = temp.prev 
        temp.prev.next = temp.next 

        temp.next = None 
        temp.prev = None 

        self.length -= 1
        return temp
    
    def reverse(self):
        current = self.head
        self.tail = self.head  
        prev_node = None

        while current is not None:
            next_node = current.next  
            current.next = prev_node  
            current.prev = next_node 

            prev_node = current  
            current = next_node  

        self.head = prev_node 

    
my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)
my_dll.append(6)
my_dll.print_list()
print("-------")
# my_dll.insert(1,6)
# my_dll.print_list()

my_dll.reverse()
my_dll.print_list()


