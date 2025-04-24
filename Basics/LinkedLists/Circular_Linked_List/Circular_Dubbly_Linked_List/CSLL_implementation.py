# Define a class Node to describe a node of a circular doubly linked list.
# Define a class CDLL to implement Circular Doubly Linked List with __init__() method to create and initialize last reference variable.
# Define a method is_empty() to check if the linked list is empty in CDLL class.
# In class CDLL, define a method insert_at_start() to insert an element at the starting of the list.
# In class CDLL, define a method insert_at_last() to insert an element at the end of the list.
# In class CDLL, define a method search() to find the node with specified element value.
# In class CDLL, define a method insert_after() to insert a new node after a given node of the list.
# In class CDLL, define a method to print all the elements of the list.
# In class CDLL, implement iterator for CDLL to access all the elements of the list in a sequence.
# In class CDLL, define a method delete_first() to delete the first element from the list.
 
# 1. Define a class Node to describe a node of a circular doubly linked list.
class Node:
    def __init__(self,item=None,prev= None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
 
#2.  Define a class CDLL to implement Circular Doubly Linked List with __init__() method to create and initialize last reference variable.
class CDLL:
    def __init__(self,start=None):
        self.start = start      
 
#3.  Define a method is_empty() to check if the linked list is empty in CDLL class.
 
    def is_empty(self):
        return self.start == None
              
#4. In class CDLL, define a method insert_at_start() to insert an element at the starting of the list.
 
    def insert_at_start(self,item):
        new_node = Node(item)
        if self.start is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.start = new_node
            return
        else:
            
            new_node.next = self.start
            new_node.prev = self.start.prev
            self.start.prev.next = new_node
            self.start.prev = new_node
            self.start = new_node
 
#5. In class CDLL, define a method insert_at_last() to insert an element at the end of the list.
 
    def insert_at_last(self,item):
        n = Node(item)
        if self.start is None:
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            n.prev.next = n
            self.start.prev = n
            
 
#6. In class CDLL, define a method insert_after() to insert a new node after a given node of the list.
 
    def insert_after(self,temp,item):
        if temp is not None:
            new_node = Node(item)
            new_node.next = temp.next
            new_node.prev =  temp
            temp.next = new_node
            temp.next.prev = new_node
            
           
#7. In class CDLL, define a method delete_at_start() element.
   
 
    def delete_at_start(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next
    
 
#8. In class CDLL, define a method delete_at_last() element.
    
    def delete_at_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
                                                                                                                                                                                                                        
#9. In class CDLL, define a method delete_item() element.
 
    def delete_item(self,item):
        if self.is_empty():
            return None
        elif self.start.item == item:
            self.delete_at_start()
        elif self.start.prev.item == item:
            self.delete_at_last()
        else:
            temp = self.start.next
            while temp is not self.start:
                if temp.item == item:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    break
                temp = temp.next
 
               
 
#10. In class CDLL, define a method to print all the elements of the list.
        
    def print_all(self):
        temp = self.start
        if temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
            while temp is not self.start:
                print(temp.item,end=' ')
                temp = temp.next
              
 
#11. In class CDLL, define a method search() to find the node with specified element value.
 
    def search(self,item):
        if self.start is None:
            return None
        temp = self.start
        if temp.item == item:
            return temp
        else:
            temp = temp.next
        while temp != self.start:
            if temp.item == item:
                return temp
            temp = temp.next
        return None    
    
    def __iter__(self):
        return CDLL_Itretor(self.start)
 
 
# In class CDLL, implement iterator for CDLL to access all the elements of the list in a sequence.
 
class CDLL_Itretor:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count ==1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next     
        return data
 
        
        
        
linklist = CDLL()
linklist.insert_at_start(36)    
linklist.insert_at_start(25)
linklist.insert_at_start(6)
linklist.insert_at_last(33)
linklist.insert_at_last(69)
linklist.insert_after(linklist.search(25),8758)
linklist.delete_at_start()
linklist.delete_at_last()
linklist.delete_item(33)
linklist.delete_item(69)
temp = linklist.search(25)
print(temp)
linklist.print_all()
print()
for x in linklist:
    print(x)