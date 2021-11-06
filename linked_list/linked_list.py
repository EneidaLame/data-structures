

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def remove(self, value):
        curr = self.head
        prev = None
        while curr is not None:
            if curr.value == value:
                if prev is None:  # we delete first element
                    self.head = curr.next
                else:
                    prev.next = curr.next
                break;
            prev = curr
            curr = curr.next

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def to_python_list(self):
        list = []
        temp = self.head
        while temp is not None:
            list.append(temp.value)
            temp = temp.next
        return list

    def __str__(self):
        return str(self.to_python_list())



list = LinkedList()
list.add(8)
list.add(9)
list.add(5)
print(list)

print("Remove 9")
list.remove(9)
print(list)

print("Remove 5")
list.remove(5)
print(list)

print("Remove 8")
list.remove(8)
print(list)