class Node:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None

n1 = Node("A")
n2 = Node("B")
n3 = Node("C")
n4 = Node("D")
n5 = Node("E")
n6 = Node("F")
n7 = Node("G")
n8 = Node("H")


n1.left_child = n2
n1.right_child = n3
n3.right_child = n6
n2.left_child = n4
n2.right_child = n5
n4.left_child = n7
n4.right_child = n8

def percorrerArvore(root: Node, Ordem):
    if root == None:
        return

    if Ordem == 'Pré':
        print(root.data)
        if root.left_child:
            percorrerArvore(root.left_child,Ordem)
        if root.right_child:
            percorrerArvore(root.right_child,Ordem)
    if Ordem == 'Em':
        if root.left_child:
            percorrerArvore(root.left_child,Ordem)
        print(root.data)
        if root.right_child:
            percorrerArvore(root.right_child,Ordem)
    if Ordem == 'Pos':
        if root.left_child:
            percorrerArvore(root.left_child,Ordem)
        if root.right_child:
            percorrerArvore(root.right_child,Ordem)
        print(root.data)

percorrerArvore(n1,'Pré')