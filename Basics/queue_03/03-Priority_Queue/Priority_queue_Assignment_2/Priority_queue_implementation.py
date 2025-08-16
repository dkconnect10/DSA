
# ========================================================
# Assignment-17: Priority queue using linked list
# ========================================================

'''
1. Define a Node class with instance member variables item, priority and next.

2. Define a class PriorityQueue to implement priority queue data structure using singly
   linked list. Provide __init__() method to create a start reference variable (initially
   containing None) and item_count variable (initially 0).

3. Define a push method in PriorityQueue class to insert new data with given priority.

4. Define a pop method in PriorityQueue class, which returns the highest priority data
   stored in the priority queue data structure. Raise exception if priority queue is empty.

5. Define is_empty method in PriorityQueue class to check if the priority queue is empty.

6. In class PriorityQueue, define a method size to return the number of elements
   present in the priority queue.
'''


class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next
        
        
class PriorityQueue:
    def __init__(self):
        self.start=None 
        self.item_count=0 
    
    
        
    def push(self,item,priority):
        n=Node(item,priority)
        if self.start is None or self.start.priority < priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next is not None and temp.next.priority>=priority:
                temp=temp.next
            n.next=temp.next   
            temp.next=n
        self.item_count+=1
                    
    
    
    def is_empty(self):
        return self.start is None
    
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")   
        data = self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data
   
    def size(self):
        return self.item_count    
        
# Test
obj = PriorityQueue()
obj.push(1, 5)   # item=1, priority=5
obj.push(8, 6)   # item=8, priority=6
print(obj.size())  # 2
print(obj.pop())   # should pop item=8 (priority=6)
print(obj.pop())   # should pop item=1 (priority=5)
print(obj.size())  # 0