
# for elemento in diccionario:
#     texto += " " + elemento + " " + diccionario[elemento]
# print(texto)

# variable: int = "hola"


# class Clase:
#     def __init__(self, arg1:int):
#         self.arg1 = arg1

#     def doble_arg1(self):
#         resp = self.arg1 * 2
#         return resp

#     def __repr__(self):
#         return f"el doble del argumento es {resp}"

# prueba1 = Clase(2)
# print(prueba1)
from src.htmlnode import LeafNode 

node = LeafNode("p", "Hello, world")
print(node.to_html())

node2 = LeafNode(None, "Hello, world")
print(node2.to_html())
