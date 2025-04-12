# 📘 Singly Linked List – DSA Using Python

## 📋 Agenda
1. What is a List?
2. What is a Node?
3. Defining a Node
4. Singly Linked List
5. Elementary Operations

---

## 1️⃣ What is a List?
A **list** is a linear collection of data items. Also referred to as **list items**.

### 🔸 Examples:
- List of marks (integers):  
  `30, 32, 20, 35, 41, 38`

- List of city names (strings):  
  `"Bhopal", "Itarsi", "Indore", "Delhi", "Jaipur", "Pune", "Gwalior", "Mumbai", "Jabalpur"`

- List of employees:
IDs: 100, 101, 102, 103, 104 Names: Savita, Akshay, Shivam, Jenit, Atul Salaries: 25000, 35000, 40000, 30000, 50000



---

## 2️⃣ What is a Node?
A **Node** is the basic unit of a Linked List.

### Each Node contains:
- `item`: actual data value
- `next`: pointer to the next node in the list

---

## 3️⃣ Defining a Node in Python

```python
class Node:
  def __init__(self, item=None, next=None):
      self.item = item
      self.next = next


4️⃣ Singly Linked List (SLL)
A Singly Linked List is a linear data structure where each node points to the next node.

Key Characteristics:
Dynamic size (can grow and shrink)

Each node holds data and a reference to the next node

Example Layout:  [Data|Next] → [Data|Next] → [Data|Next] → None


5️⃣ Elementary Operations on SLL
Operation	Description
insert_at_start()	Inserts a new node at the beginning
insert_at_last()	Inserts a new node at the end
delete_first()	Deletes the first node from the list
is_empty()	Checks whether the list is empty
traverse()	Prints all items in the linked list