
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
    def __init__(self,start=None):
        self.start=start 
        self.item_count=0 
        
    def push(self,item,priority):
        n=Node(item,priority,None)
        temp=self.start
        while temp.priority>self.priority:
            temp.next
        n.next=temp.next
        temp=n
        self.item_count+=1
    
    
    def is_empty(self):
        return self.item_count==0
    
        
    def size(self):
        return self.item_count    
        
obj=PriorityQueue()
obj.push(1,5)
obj.push(8,6)  
obj.size()                    