
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def insert(root,node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inOrden(root):
    if root is not None:
        inOrden(root.left)
        result = min_operations(root)
        print("El nodo de valor", root.value, "da", result)
        inOrden(root.right)


# encontrar el mínimo número de operaciones

def min_operations(root):
    if root is not None:
        if root.value == 1:
            return 1
        elif root.value % 2 == 0:
            return 1 + min_operations(Node(root.value // 2))  # Crear un nuevo nodo con el valor
        else:
            
            return 1 + min_operations(Node(root.value - 1))  # Crear un nuevo nodo con el valor - 1
       
root = Node(7)
insert(root, Node(8))
insert(root, Node(5))
insert(root, Node(4))

inOrden(root)
print("El nodo de valor", root.value, "da", min_operations(root))
print("El nodo de valor", Node(8).value, "da", min_operations(Node(8)))

