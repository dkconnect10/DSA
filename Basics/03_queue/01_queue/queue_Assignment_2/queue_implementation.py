# ========================================
# Assignment: Queue Extending List
# ========================================

"""
1. Define a class Queue to implement queue data structure by extending the list class.

2. Define a method is_empty() to check if the queue is empty in the Queue class.

3. In Queue class, define enqueue() method to add data to the rear of the queue.

4. In Queue class, define dequeue() method to remove data from the front of the queue.

5. In Queue class, define front() method to return the front element of the queue.

6. In Queue class, define size() method to return the size of the queue (i.e., number of items present in the queue).

7. Implement a way to restrict use of insert(), pop(index), or reverse() method of list class from the queue object.
"""



class Queue(list):
    
    def is_empty(self):
        return len(self)==0
    
    def enqueue(self,data):
        self.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            return super().pop(0)
        else:
            raise IndexError("Queue is empty")
        
    def front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Queue is empty")
        
    def rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Queue is empty")
        
    def size(self):
        return len(self)  
    
    def insert(self,index,Value):
        raise NotImplementedError("insert() is not allowed for Queue.")  
    
    def pop(self,index=None):
        if index is None:
            return super().pop()
        raise NotImplementedError("pop() is not allowed for Queue.")
    
    def reverse(self):
        raise NotImplementedError("reverse() is not allowed for Queue.")
    
    
obj = Queue()
obj.enqueue(30)
obj.enqueue(20)
obj.enqueue(10)
print("Total size of Queue",obj.size())
print("Front Value of queue",obj.front())
print("rear Value of Queue",obj.rear())
obj.dequeue()
print("Total size of Queue",obj.size())
print("Front Value of queue",obj.front())
print("rear Value of Queue",obj.rear())  


###
# obj.insert(5,6)  
# obj.pop(0)
# obj.reverse()
            
                    