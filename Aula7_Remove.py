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
        if pointer:
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
        print('None')

    def __len__(self):
        return self.size

    def get(self, index):
        pointer = self.head
        if index < 0 or index > self.size:
            return None
        for x in range(index):
            pointer = pointer.next
        return pointer.data

    def set(self, index, value):
        pointer = self.head
        if index < 0 or index > self.size:
            return None
        for x in range(index):
            pointer = pointer.next
        pointer.data = value

    def remove(self, value):
        pointer = self.head
        if not self.head:
           raise IndexError("A lista está vazia")
        if value == self.head.data:
            self.head = self.head.next
            self.size -= 1
            return

        while pointer.next:
            if pointer.next.data == value:
                pointer.next = pointer.next.next
                self.size -= 1
                return
            pointer = pointer.next

    def remove_index(self, index):
        pointer = self.head
        if index < 0 or index >= self.size:
            raise IndexError("Índice inválido")
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        ###


lista = LinkedList()
lista.append(10)
lista.append(20)
lista.append(31)
print(lista.get(1))
lista.display()
lista.set(2, 30)
lista.display()
lista.remove(20)
lista.display()