class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0

    def len(self):
        return self.__size

    def __len__(self):
        return self.__size

    def append(self, elemento):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elemento)
        else:
            self.head = Node(elemento)
        self.__size += 1

    def display(self):
        pointer = self.head
        while pointer:
            print(pointer.data, end='-> ')
            pointer = pointer.next


lista = LinkedList()
lista.append(10)
lista.append(20)
lista.append(30)
print(lista.display())
print(len(lista))
print(lista.len())


