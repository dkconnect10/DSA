# =======================================
# Objective: Implement Queue using SLL
# =======================================

# 1. Import the module that contains your Singly Linked List (SLL) class.
#    This SLL should support basic operations like insertion at the end,
#    deletion from the beginning, and size tracking.

# 2. Define a class `Queue` to implement the queue data structure.

# 3. In the `__init__()` method of `Queue`, create an instance of your
#    SinglyLinkedList class.

# 4. Define a method `is_empty()` in the `Queue` class to check whether the queue is empty
#    by using the linked list's size or head pointer.

# 5. Define a method `enqueue(data)` in the `Queue` class to insert an element
#    at the rear of the queue (use the linked list's insert_at_end or similar method).

# 6. Define a method `dequeue()` in the `Queue` class to remove and return the
#    front element of the queue (use the linked list's delete_from_start or similar method).

# 7. Define a method `peek()` in the `Queue` class to return the front element
#    without removing it (access the head node of the linked list).

# 8. Define a method `size()` in the `Queue` class to return the total number of
#    elements in the queue (use the linked list's size property or method).


from Basics.LinkedLists_01.singleLinkList.SLL_implementation import *

class Queue:
    def __init__(self):
        self.mylist = SLL()
        self.item_count=0
        
    def is_empty(self):
        return self.mylist.is_empty()
    
    def enqueue(self,data):
        self.mylist.insert_at_end(data)
        self.item_count+=1
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        else:
            self.mylist.delete_from_start()
            self.item_count-=1
            
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
        else:
            raise IndexError("queue is empty")
        
    def size(self):
        return self.item_count                    


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.peek())         # Output: 10
print("Dequeued:", q.dequeue())   # Output: 10
print("New Front:", q.peek())     # Output: 20
print("Queue Size:", q.size())    # Output: 2
        