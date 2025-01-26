diccionario:dict = { "href":"http", "href2":"http2"}
texto:str = ""
for elemento in diccionario:
    texto += " " + elemento + " " + diccionario[elemento]
print(texto)

variable: int = "hola"


class Clase:
    def __init__(self, arg1:int):
        self.arg1 = arg1

    def doble_arg1(self):
        resp = self.arg1 * 2
        return resp

    def __repr__(self):
        return f"el doble del argumento es {resp}"

prueba1 = Clase(2)
print(prueba1)
