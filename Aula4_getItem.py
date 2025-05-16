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
            return None
        for _ in range(index):
            pointer = pointer.next
        return pointer.data

    def get2(self, index):
        if index < 0 or index >= self._size:
            return None
        pointer = self.head
        count = 0
        while pointer:
            if count == index:
                return pointer.data
            count += 1
            pointer = pointer.next
        return None

    def get3(self, index):
        pointer = self.head
        if index < 0 or index >= self._size:
            raise IndexError("Erro de índice")
        for x in range(index):
            pointer = pointer.next
        return pointer.data

    def get4(self, index):
        pointer = self.head
        for x in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Erro")
        return pointer.data


lista = LinkedList()
lista.append(10)
lista.append(20)
lista.append(30)
lista.display()
print(lista.get(2))
