# ========================================
# Assignment 13: Queue using Linked List Concept
# ========================================

"""
1. Define a class Queue to implement the queue data structure using the singly linked list concept.
   Define the __init__() method to initialise 'front' and 'rear' reference variables and 
   an 'item_count' variable to keep track of the number of elements in the queue.

2. Define a method is_empty() in the Queue class to check whether the queue is empty.

3. In the Queue class, define an enqueue() method to insert a new element at the rear of the queue.

4. In the Queue class, define a dequeue() method to remove and return the element from the front of the queue.

5. In the Queue class, define a peek() method to return the front element of the queue without removing it.

6. In the Queue class, define a size() method to return the total number of items in the queue.
"""


class Node:
   def __init__(self,item=None,next=None):
      self.item=item
      self.next=next
   

class Queue:
   def __init__(self):
      self.front=None
      self.rear=None
      self.item_count=0
      
   def is_empty(self):
      return self.front==None
   
   def enqueue(self,data):
      n = Node(data)
      if self.is_empty():
         self.front = n
      else:
         self.rear.next =n
      self.rear = n       
      self.item_count += 1

   def dequeue(self):
      if self.is_empty():
         raise IndexError("Queue is empty")
      elif self.front==self.rear:
         self.front=None
         self.rear=None
      else:
         self.front=self.front.next   
      self.item_count -= 1   
      
      
   def peek(self):
      if self.is_empty():
         raise IndexError("Queue is empty")
      else:
         return self.front.item
      
   def size(self):
      return self.item_count 
   
   
   
# ========== TESTING ==========
obj = Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)

print("Peek:", obj.peek()) 
print("Front:", obj.front.item, "Rear:", obj.rear.item)

obj.dequeue()

print("Front after dequeue:", obj.front.item, "Rear:", obj.rear.item)
print("Queue size:", obj.size())    