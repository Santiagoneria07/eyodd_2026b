# Creando la clase nodo
class Node:
    # Constructor 
    def __init__(self, data=None):
        self.data = data
        self.next = None 
    def iter(self):
        current = self
        while current:
            value = current.data
            current = current.next
            yield value 


# Creando una funcion pricipal 
def main ():
    # Codigo de prueba

    # Testear nuestra clase nodo
    node_01 = Node("eggs")
    node_02 = Node("hem")
    node_03 = Node("bacon")

    #print("📎NODOS SIN ENLAZAR")
    #print (f"node 01: D:{node_01.data }- N:{node_01.next}")
    #print (f"node 02: D:{node_02.data }- N:{node_02.next}")
    #print (f"node 03: D:{node_03.data }- N:{node_03.next}")

    # Enlazando los nodos 
    node_01.next = node_02
    node_02.next = node_03

    #print("📎NODOS ENLAZADOS")
    #print (f"node 01: D:{node_01.data }- N:{node_01.next}")
    #print (f"node 02: D:{node_02.data }- N:{node_02.next}")
    #print (f"node 03: D:{node_03.data }- N:{node_03.next}")

    # List Traversal (Recorrido de la lista)
    current = node_01
    # for se define la candida de veces de repeticion 
    # while: no esta definido la cantida de veces de repeticion 
    # hasta tener la condicion (None)

    for node_val in node_01.iter():
        print(node_val)

# Invocando a Main 
if __name__ == "__main__":
    main()