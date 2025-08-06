
# =========================================================
# Assignment-15: Deque using Doubly Linked List Concept
# =========================================================

# 1. Define a class Node with instance object member variables prev, item and next.

# 2. Define a class Deque to implement deque data structure using doubly linked list
#    concept. Define __init__() method to initialise front and rear reference variable; and
#    item_count variable to keep track of number of elements in the deque.

# 3. Define a method is_empty() to check if the deque is empty in Deque class.

# 4. In Deque class, define insert_front() method to add data at the front of the deque.

# 5. In Deque class, define insert_rear() method to add data at the rear of the deque.

# 6. In Deque class, define delete_front() method to remove front element from the
#    deque.

# 7. In Deque class, define delete_rear() method to remove rear element from the deque.

# 8. In Deque class, define get_front() method to return front element of the deque.

# 9. In Deque class, define get_rear() method to return rear element of the deque.

# 10. In Deque class, define size() method to return size of the deque that is number of
#     items present in the deque.



class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
    
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
        
    def is_empty(self):
        return self.item_count == 0
    
    def insert_front(self,data):
        n = Node(None,data,self.front)
        if self.is_empty():
            self.rear=n    
        else:
            self.front.prev=n
        self.front=n
        self.item_count += 1 
            
      
        
    def insert_rear(self,data):
        n = Node(self.rear,data,None)
        if self.is_empty(): 
            self.front=n
        elif self.front == self.rear:
            self.front.next=n        
        else:
            self.rear.next=n
        self.rear=n 
        self.item_count += 1   
            
     
    def delete_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        elif self.front == self.rear:
            self.rear=None
            self.front=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count -= 1        
        
    def delete_rear(self):
            if self.is_empty():
                raise IndexError("deque is empty")
            elif self.front == self.rear:
                self.rear=None
                self.front=None
            else:
                self.rear=self.rear.prev
                self.rear.next=None
            self.item_count -= 1
             
                
    def get_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            return self.front.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count
    
    
    
# Test Code
obj = Deque()
obj.insert_front(10)
obj.insert_front(20)
obj.insert_rear(30)
obj.insert_rear(40)
print(obj.get_front(), obj.get_rear())  # 20 40
obj.delete_front()
obj.delete_rear()
print(obj.get_front(), obj.get_rear())  # 10 30
print(obj.size())   
        
            
            
        
        
                    
    
                    
            
            
                        
         
            
 
        
                
               
    
       
            