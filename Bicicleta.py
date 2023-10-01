# Clase hija que solo hereda de la clase padre Transporte, teniendo casi todos sus atributos por ella sola, sino es por decir todos

from Transporte import Transporte


class Bicicleta(Transporte):
    def __init__(self, aro, peso, precio, marca):
        Transporte.__init__(self)
        self.__aro = aro
        self.__peso = peso
        self.__marca = marca
        self.__precio = precio

    def get_aro(self):
        return self.__aro

    def set_aro(self, aro):
        self.__aro = aro

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def valor_por_kilogramo(self):
        return 400

    def calcularDespacho(self):
        costo_despacho = self.get_despacho() + \
            self.__peso * self.valor_por_kilogramo()
        return costo_despacho

    def imprimirCaracteristicas(self):
        print("Características de la Bicicleta:")
        caracteristicas = f"Aro: {self.__aro}\n"
        caracteristicas += f"Peso: {self.__peso} kg\n"
        caracteristicas += f"Precio: ${self.__precio}\n"
        caracteristicas += f"Marca: {self.__marca}\n"
        return caracteristicas
