# 1. Define a class `Node` to describe a node of a circular linked list.

class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
        
        
        
# 2. Define a class `CLL` to implement Circular Linked List with `__init__()` method to create and initialize the `last` reference variable.

        
class CLL:
    def __init__(self,last=None):
        self.last = last
        
        
# 3. Define a method `is_empty()` to check if the linked list is empty in the `CLL` class.
    def is_empty(self):
        return self.last == None
    
# 4. In class `CLL`, define a method `insert_at_start()` to insert an element at the start of the list.


    def insert_at_start(self,item):
        new_node = Node(item)
        if self.last is None:
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next 
            self.last.next = new_node
            
# 5. In class `CLL`, define a method `insert_at_last()` to insert an element at the end of the list.
            
    def insert_at_last(self,item):
        new_node = Node(item)
        if self.is_empty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node  
            self.last = new_node  
            
# 10. In class `CLL`, define a method `delete_first()` to delete the first element from the list.

    def delete_first(self):
        temp = self.last
        if temp is None:
            return
        else:
            self.last.next = self.last.next.next
            
# 11. In class `CLL`, define a method `delete_last()` to delete the last element from the list.

    def delete_last(self):
        pass
            



                
                
            
           
        
# 8. In class `CLL`, define a method to print all the elements of the list.
  
    def print_list(self):
        if self.last is not None:
            temp = self.last.next
            while temp is not None:
                print(temp.item,end=" ")
                temp = temp.next   
                if temp == self.last.next:
                    break     
    
        
linklist = CLL()
linklist.insert_at_start(24)
linklist.insert_at_start(67)
linklist.insert_at_start(2)
linklist.insert_at_start(9)
linklist.insert_at_last(25)
linklist.insert_at_last(0)
linklist.insert_at_last(88)
linklist.delete_first()
linklist.print_list()
print()
       