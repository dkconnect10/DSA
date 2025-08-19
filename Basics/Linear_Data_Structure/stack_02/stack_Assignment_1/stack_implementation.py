
# DSA using Python

# Define a class Stack
# Implement a stack data structure using a list. Define the __init__() method to create an empty list object as an instance object member of the Stack class.

class Stack:
    def __init__(self):
        self.item = []
    
        
        
        
        
    
# Define is_empty() method
# Create a method is_empty() to check if the stack is empty.
    def is_empty(self):
        return len(self.item)==0
    
    



# Define push() method
# Add the push() method in the Stack class to insert data onto the stack.

    def push(self,item):
        self.item.append(item)

# Define pop() method
# Create the pop() method in the Stack class to remove the top element from the stack.

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is empty")

# Define peek() method
# Create the peek() method in the Stack class to return the top element of the stack without removing it.

    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Stack is empty")

# Define size() method
# Create the size() method in the Stack class to return the number of items present in the stack.


    def size(self):
       return len(self.item)
       
       
       
newlist = Stack()
newlist.push(5)
newlist.push(6)
newlist.push(7)
newlist.push(8)
newlist.push(9)
newlist.is_empty()
print("top element is this:",newlist.peek())
print("remove last item :",newlist.pop())
print("top element is this:",newlist.peek())
newlist.size()
       