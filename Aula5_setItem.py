class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, elemento):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elemento)
        else:
            self.head = Node(elemento)
        self._size += 1

    def display(self):
        pointer = self.head
        while pointer:
            print(pointer.data, end='->')
            pointer = pointer.next
        print("None")

    def get(self, index):
        pointer = self.head
        if index < 0 or index >= self._size:
            raise IndexError("Erro de índice")
        for x in range(index):
            pointer = pointer.next
        return pointer.data

    def set(self, index, elem):
        pointer = self.head
        if index < 0 or index >= self._size:
            raise IndexError("Erro de índice")
        for x in range(index):
            pointer = pointer.next
        pointer.data = elem

    def __index__(self):
        pointer = self.head
        index = 0
        while pointer:
            print(f'Index: {index}, Value: {pointer.data}')
            pointer = pointer.next
            index += 1

    def index(self, elem):
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        return None


lista = LinkedList()
lista.append(10)
lista.append(20)
lista.append(30)
lista.display()
print(lista.get(2))
lista.set(0, 50)
lista.display()
print(lista.index(20))