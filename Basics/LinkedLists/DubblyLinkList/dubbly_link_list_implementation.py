"""
Assignment-4: Doubly Linked List

1. Define a class Node to describe a node of a doubly linked list.
2. Define a class DLL to implement Doubly Linked List with __init__() method to create and initialise start reference variable.
3. Define a method is_empty() to check if the linked list is empty in DLL class.
4. In class DLL, define a method insert_at_start() to insert an element at the starting of the list.
5. In class DLL, define a method insert_at_last() to insert an element at the end of the list.
6. In class DLL, define a method search() to find the node with specified element value.
7. In class DLL, define a method insert_after() to insert a new node after a given node of the list.
8. In class DLL, define a method to print all the elements of the list.
9. In class DLL, implement iterator for DLL to access all the elements of the list in a sequence.
"""




class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
 
 
class DoublyLinkedList:
    def __init__(self, start=None):
        self.start = start
 
    def is_empty(self):
        return self.start is None
 
    def insert_first(self, data):
        new_node = Node(None, data, self.start)
        if self.start is not None:
            self.start.prev = new_node
        self.start = new_node
 
    def insert_last(self, data):
        new_node = Node(None, data, None)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
 
    def print_list(self):
        if self.start is not None:
            temp = self.start
            count = 0
            while temp is not None:
                print(temp.data, end=" <-> ")
                count += 1
                temp = temp.next
            print("None")
            print("Count of the list:", count)
        else:
            print("List is empty")
 
    def search_node(self, data):
        temp = self.start
        if self.is_empty():
            print("List is empty")
        else:
            while temp is not None:
                if temp.data == data:
                    print("Matched value node:", temp.data)
                    return temp
                temp = temp.next
            print("Value not found")
            return None
 
    def insert_after(self, temp, data):
        current = self.start
        while current is not None:
            if current == temp:
                new_node = Node(temp, data, temp.next)
                if temp.next is not None:
                    temp.next.prev = new_node
                temp.next = new_node
                break
            current = current.next
   
    def delete_first(self):
        temp = self.start
        if not self.is_empty():
            self.start = temp.next
            temp.next.prev = None
            
    def delete_last(self):
        if self.start is None:
            return None
        elif self.start.next is None:
            self.start = None
        else:    
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None      
            
    def delete_item(self,data):
        
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.data == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break       
                temp = temp.next    
 
    def __iter__(self):
        return DLLItertor(self.start)
 
 
class DLLItertor:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data                   
 
                
                
            
             
                           
            
            
        
 
 
newobj = DoublyLinkedList()
newobj.insert_first(10)
newobj.insert_first(25)
newobj.insert_first(36)
newobj.insert_first(66)
newobj.insert_last(100)
 
print("Initial List:")
newobj.print_list()
 
 
temp_node = newobj.search_node(25)
if temp_node:
    newobj.insert_after(temp_node, 105)
 
newobj.delete_first()
newobj.delete_last()
newobj.print_list()
newobj.delete_item(25)
newobj.print_list()
 
objs = DLLItertor(newobj.start)
 
for i in objs:
    print(i)
 