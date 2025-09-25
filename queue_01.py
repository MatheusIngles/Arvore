import queue

class Node:
    def __init__(self, valoe):
        self.valoe = valoe
        self.left_child = None
        self.right_child = None
        self.altura = None

def calcularAltura(root, altura = 0):
    arvore_de_caminhada =  root
    arvore_de_caminhada.altura = altura
    if arvore_de_caminhada.left_child:
        calcularAltura(arvore_de_caminhada.left_child, altura +1)
    if arvore_de_caminhada.right_child:
        calcularAltura(arvore_de_caminhada.right_child, altura+1)

def bft(root):
    if not root:
        return True

    fifo = queue.Queue()
    fifo.put(root)
    quantidade_por_nivel= 0
    while not fifo.empty():
        no = fifo.get()
        print(no.valoe, end=" ")
        if no.left_child:
            quantidade_por_nivel+= 1
            fifo.put(no.left_child)
        if no.right_child:
            quantidade_por_nivel+= 1
            fifo.put(no.right_child)

def dft(root):
    if not root:
        return True

    Lifo = queue.LifoQueue()
    Lifo.put(root)

    while not Lifo.empty():
        no = Lifo.get()
        print(no.valoe, end=" ")
        if no.right_child:
            Lifo.put(no.right_child)
        if no.left_child:
            Lifo.put(no.left_child)

        
root =  Node(1)
root.left_child = Node(2)
root.right_child = Node(3)
root.left_child.left_child = Node(4)
root.left_child.right_child = Node(5)
root.right_child.left_child = Node(6)
root.right_child.right_child = Node(7)

bft(root)
print("\n-----------------------")
dft(root)