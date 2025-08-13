
# ====================================================
# Assignment-14: Deque Implementation using List
# ====================================================


# 1. Define a class Deque to implement deque data structure using list. Define `__init__()` method 
#     to create an empty list object as instance object member of Deque.

# 2. Define a method `is_empty()` to check if the deque is empty in Deque class.

# 3. In Deque class, define `insert_front()` method to add data at the front end of the deque.

# 4. In Deque class, define `insert_rear()` method to add data at the rear end of the deque.

# 5. In Deque class, define `delete_front()` method to remove front element from the deque.

# 6. In Deque class, define `delete_rear()` method to remove rear element from the deque.

# 7. In Deque class, define `get_front()` method to return front element of the deque.

# 8. In Deque class, define `get_rear()` method to return rear element of the deque.

# 9. In Deque class, define `size()` method to return size of the deque that is number of items 
#    present in the deque.


class Deque:
    def __init__(self):
        self.mylist = []
        
    def is_empty(self):
        return len(self.mylist)==0
    
    def insert_front(self,data):
        if data is not None:
            self.mylist.insert(0,data)
        else:
            raise IndexError("Data is empty")
        
    def insert_rear(self,data):
        if data is not None:
          self.mylist.append(data)
        else:
            raise IndexError("Data is empty")
        
    def delete_front(self):
        if not self.is_empty():
          self.mylist.pop(0)
        else:
            raise IndexError("deque is empty")
        
    def delete_rear(self):
        if not self.is_empty():
          self.mylist.pop(-1)
        else:
            raise IndexError("deque is empty")
        
    def get_front(self):
        if not self.is_empty():
           return self.mylist[0]
        else:
            raise IndexError("deque is empty") 
        
    def get_rear(self):
        if not self.is_empty():
          return self.mylist[-1]
        else:
            raise IndexError("deque is empty")       
                                
                                
    def size(self):
        return len(self.mylist)
    
    
    
                                
dq = Deque()

dq.insert_rear(10)
dq.insert_rear(20)
dq.insert_front(5)

print("Front:", dq.get_front())   
print("Rear:", dq.get_rear())     
print("Size:", dq.size())         

dq.delete_front()
dq.delete_rear()

print("Front after deletion:", dq.get_front())  
print("Size after deletion:", dq.size())        
        