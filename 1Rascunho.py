class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        pointer = self.head
        if self.head:
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(value)
        else:
            self.head = Node(value)
        self.size += 1

    def display(self):
        pointer = self.head
        while pointer:
            print(pointer.data, end='-> ')
            pointer = pointer.next
        print("None")

    def get(self, index):
        pointer = self.head
        if index < 0 or index >= self.size:
            return None
        for _ in range(index):
            pointer = pointer.next
        return pointer.data


lista = LinkedList()
lista.append(10)
lista.append(20)
lista.append(30)
lista.display()
print(lista.get(3))

