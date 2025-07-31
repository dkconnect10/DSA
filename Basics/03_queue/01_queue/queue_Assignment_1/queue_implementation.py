# -----------------------------------------------------------
# Assignment-12: Queue using List
# -----------------------------------------------------------


# 1. Define a class `Queue` to implement the queue data structure using a list.
#    Define `__init__()` method to create an empty list object as an instance member of Queue.

# 2. Define a method `is_empty()` to check if the queue is empty in the Queue class.

# 3. In the Queue class, define the `enqueue()` method to add data at the rear end of the queue.

# 4. In the Queue class, define the `dequeue()` method to remove the front element from the queue.

# 5. In the Queue class, define the `get_front()` method to return the front element of the queue.

# 6. In the Queue class, define the `get_rear()` method to return the rear element of the queue.

# 7. In the Queue class, define the `size()` method to return the size of the queue
#    (i.e., the number of items present in the queue).


class Queue:
    def __init__(self):
        self.mylist = []
        
    def is_empty(self):
        return len(self.mylist)==0
    
    def enqueue(self,data):
        self.mylist.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            self.mylist.pop(0)
        else:
            raise IndexError("Queue is empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError("Queue is emapty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            raise IndexError("Queue is emapty")
        
    def size(self):
        return len(self.mylist) 
    
    
obj = Queue()
obj.enqueue(30)
obj.enqueue(20)
obj.enqueue(10)
print("Total size of Queue",obj.size())
print("Front Value of queue",obj.get_front())
print("rear Value of Queue",obj.get_rear())
obj.dequeue()
print("Total size of Queue",obj.size())
print("Front Value of queue",obj.get_front())
print("rear Value of Queue",obj.get_rear())
       
                
        
                