# # Assignment-5: Circular Linked List (DSA using Python)
 
# ## Questions
 
# 1. Define a class `Node` to describe a node of a circular linked list.
# 2. Define a class `CLL` to implement Circular Linked List with `__init__()` method to create and initialize the `last` reference variable.
# 3. Define a method `is_empty()` to check if the linked list is empty in the `CLL` class.
# 4. In class `CLL`, define a method `insert_at_start()` to insert an element at the start of the list.
# 5. In class `CLL`, define a method `insert_at_last()` to insert an element at the end of the list.
# 6. In class `CLL`, define a method `search()` to find the node with a specified element value.
# 7. In class `CLL`, define a method `insert_after()` to insert a new node after a given node in the list.
# 8. In class `CLL`, define a method to print all the elements of the list.
# 9. In class `CLL`, implement an iterator for CLL to access all the elements of the list in a sequence.
# 10. In class `CLL`, define a method `delete_first()` to delete the first element from the list.
# 11. In class `CLL`, define a method `delete_last()` to delete the last element from the list.
 
 
# 1. Define a class `Node` to describe a node of a circular linked list.
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


# 2. Define a class `CLL` to implement Circular Linked List with `__init__()` method to create and initialize the `last` reference variable.
class CLL:
    def __init__(self, last=None):
        self.last = last

    # 3. Define a method `is_empty()` to check if the linked list is empty in the `CLL` class.
    def is_empty(self):
        return self.last is None

    # 4. In class `CLL`, define a method `insert_at_start()` to insert an element at the start of the list.
    def insert_at_start(self, item):
        new_node = Node(item)
        if self.last is None:
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node

    # 5. In class `CLL`, define a method `insert_at_last()` to insert an element at the end of the list.
    def insert_at_last(self, item):
        new_node = Node(item)
        if self.is_empty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    # 6. In class `CLL`, define a method `search()` to find the node with a specified element value.
    def search(self, item):
        if self.last is None:
            return None
        temp = self.last.next
        while True:
            if temp.item == item:
                return temp
            temp = temp.next
            if temp == self.last.next:
                break
        return None

    # 7. In class `CLL`, define a method `insert_after()` to insert a new node after a given node in the list.

    def insert_after(self,temp,item):
        if temp is not None:
            new_node = Node(item,temp.next)
            temp.next = new_node
            if temp == self.last:
                self.last = new_node
        return None                
        
        
        
        

    # 8. In class `CLL`, define a method to print all the elements of the list.
    def print_list(self):
        if self.last is not None:
            temp = self.last.next
            while True:
                print(temp.item, end=" ")
                temp = temp.next
                if temp == self.last.next:
                    break

    def __iter__(self):
        return CLLIterator(self.last)

    # 10. In class `CLL`, define a method `delete_first()` to delete the first element from the list.
    def delete_first(self):
        if self.last is None:
            return
        elif self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next

    # 11. In class `CLL`, define a method `delete_last()` to delete the last element from the list.
    def delete_last(self):
        if self.last is None:
            return
        elif self.last.next == self.last:
            self.last = None
        else:
            temp = self.last.next
            while temp.next != self.last:
                temp = temp.next
            temp.next = self.last.next
            self.last = temp


# 9. In class `CLL`, implement an iterator for CLL to access all the elements of the list in a sequence.
class CLLIterator:
    def __init__(self, last):
        self.last = last
        self.start = last.next if last else None
        self.current = self.start
        self.first_pass = True if self.start else False

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None or (self.current == self.start and not self.first_pass):
            raise StopIteration
        item = self.current.item
        self.current = self.current.next
        self.first_pass = False
        return item


# Test and demo the Circular Linked List
linklist = CLL()
linklist.insert_at_start(24)
linklist.insert_at_start(67)
linklist.insert_at_start(2)
linklist.insert_at_start(9)
linklist.insert_at_last(25)
linklist.insert_at_last(0)
linklist.insert_at_last(88)
linklist.insert_after(linklist.search(67),99)
linklist.delete_first()
linklist.search(24)
print()
linklist.print_list()
print()

       
 
 