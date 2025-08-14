#==============================================================
# Assignment-16: Priority queue using list
#==============================================================

'''
1. Define a class PriorityQueue to implement priority queue data structure using list.
   Provide __init__() method to create a list object (initially empty).

2. Define a push method in PriorityQueue class to insert new data with given priority.

3. Define a pop method in PriorityQueue class, which returns the highest priority data
   stored in the priority queue data structure. Raise exception if priority queue is empty.

4. Define is_empty method in PriorityQueue class to check if the priority queue is empty.

5. In class PriorityQueue, define a method size to return the number of elements
   present in the priority queue.
   
'''


class Pq:
    def __init__(self):
        self.mylist=[]
        
    def push(self,data,priority):
        try:
            index=0
            while index<len(self.mylist) and self.mylist[index][1]>=priority:
               index+=1
               print("save")
            self.mylist.insert(index,(data,priority))      
        except Exception as e :
            print("raise error")
            return str(e)    
    
    def is_empty(self):
        return len(self.mylist)==0          
        
    def pop(self):
        if not self.is_empty():
            return self.mylist.pop(0)[0]
        raise IndexError("Priority Queue is empty")    
        
    
    
    def size(self):
        return len(self.mylist) 
    
    
obj=Pq()    
obj.push(5, 7)
obj.push(8, 1)
obj.push(9, 10)
print("Size of PQ",obj.size())

print(obj.pop())  # 9 (priority 10)
print(obj.pop())  # 5 (priority 7)
print(obj.pop())  # 8 (priority 1)

print("After Pop PQ size",obj.size())
