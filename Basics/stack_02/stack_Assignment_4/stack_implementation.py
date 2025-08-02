# -----------------------------------------------------------
# Assignment-10: Stack using Linked List (DSA using Python)
# -----------------------------------------------------------

# 1. Import module containing singly linked list code in your python file.

# 2. Define a class Stack to implement stack data structure.
#    Define __init__() method to create Singly Linked List (SLL) object.

# 3. Define a method is_empty() to check if the stack is empty in Stack class.

# 4. In Stack class, define push() method to add data onto the stack.

# 5. In Stack class, define pop() method to remove top element from the stack.

# 6. In Stack class, define peek() method to return top element on the stack.

# 7. In Stack class, define size() method to return size of the stack 
#    i.e. number of items present in the stack.
 

class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0
        
    def is_empty(self):
        return self.start is None
    
    def push(self,item):
        n = Node(item,self.start)
        self.start = n
        self.item_count += 1
        return f"pushed item , {item}"
    
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return f" poped item , {data}"
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return self.item_count  
        
        
        
obj = Stack()
print(obj.push(30)) 
print(obj.push(20))  
print(obj.push(10))  
print(obj.peek())   
print(obj.pop())  
print(obj.peek())   
print("Size:", obj.size()) 
              
            