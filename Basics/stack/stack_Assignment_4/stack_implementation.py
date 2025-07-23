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




class Stack(linklist):
    def is_empty(self):
        return len(self)==None
    
    def 