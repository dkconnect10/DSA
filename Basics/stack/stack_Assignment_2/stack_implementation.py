# 1. Define a class Stack to implement stack data structure by extending the list class
# 2. Define a method is_empty() to check if the stack is empty in the Stack class.
# 3. In Stack class, define push() method to add data onto the stack.
# 4. In Stack class, define pop() method to remove top element from the stack.
# 5. In Stack class, define peek() method to return top element on the stack.
# 6. In Stack class, define size() method to return size of the stack
#            (i.e., number of items present in the stack).

# 7. Implement a way to restrict use of insert() method of list class from stack object.



class Stack(list): 
    # is_empty()    
    def is_empty(self):
        return len(self)==0
            
            
    # define push()        
    def push(self,item):
        self.append(item)
        
        
    # define pop()
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("stack is empty")
        
            
    # define peek()
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
        
    # define size()
    def size(self):
            return len(self)
        
    
    def insert(self,index,value):
        raise AttributeError("No attribute 'insert' in stack ")    
        
            
obj = Stack()
obj.push(6)
obj.push(5)
obj.push(8)
obj.push(7)
print(obj.is_empty())  
print(obj.peek())     
print(obj.pop())       
print(obj.size())      
obj.insert(0, 99) 
       
        
            