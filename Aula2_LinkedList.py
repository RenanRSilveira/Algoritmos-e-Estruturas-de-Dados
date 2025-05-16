class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#Criando uma lista vazia:
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, elem):
        if self.head:
            #Quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)

        else:
            #Se a lista estiver vazia, adiciona o elem como head
            self.head = Node(elem)
        self.size += 1

    def len(self):
        return self.size


lista = LinkedList()
lista.append(10)
lista.append(20)
lista.append(30)
print(lista.head.data)
print(f'Tamanho da lista: {lista.len()}')