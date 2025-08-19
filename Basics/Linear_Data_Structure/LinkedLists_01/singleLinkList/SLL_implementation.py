""" Singly Linked List """

# 1. Define a class Node
#    Define a class `Node` to describe a node of a singly linked list.
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


# 2. Define a class SLL (Singly Linked List)
#    Define a class `SLL` to implement Singly Linked List with the `__init__()` method
#    to create and initialize the start reference variable.
class SLL:
    def __init__(self, start=None):
        self.start = start

    # 3. Define a method is_empty()
    def is_empty(self):
        return self.start is None

    # 4. insert_at_start()
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    # 5. insert_at_last()
    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    # 6. search()
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    # 7. insert_after()
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    # 8. print_all()
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    # 10. delete_first()
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    # 11. delete_last()
    def delete_last(self):
        if self.start is None:
            return
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    # 12. delete_item()
    def delete_item(self, data):
        if self.start is None:
            return
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    # 9. iterator
    def __iter__(self):
        return SLLIterator(self.start)


class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# Driver Code
mylist = SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20), 25)
mylist.print_list()

mylist.delete_item(30)
print()

for x in mylist:
    print(x, end=' ')

print()
