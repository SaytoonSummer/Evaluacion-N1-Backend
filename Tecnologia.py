# Clase padre que va a heredar a sus hijas Scooter, Tv y Consola, la clase mas importante de todas vaya.

class Tecnologia:

    def __init__(self, marca, voltaje, precio, eficiencia):
        self.__marca = marca
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia

    def calcular_descuento(self):
        if self.__eficiencia in ["A", "B"]:
            print("Su descuento por eficiencia es del 50%")
            return 0.5
        elif self.__eficiencia in ["C", "D"]:
            print("Su descuento por eficiencia es del 30%")
            return 0.3
        elif self.__eficiencia in ["E", "F"]:
            print("Su descuento por eficiencia es del 10%")
            return 0.1
        else:
            print("Su descuento por eficiencia no aplica en este caso")
            return 0

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_voltaje(self):
        return self.__voltaje

    def set_voltaje(self, voltaje):
        self.__voltaje = voltaje

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def get_eficiencia(self):
        return self.__eficiencia

    def set_eficiencia(self, eficiencia):
        self.__eficiencia = eficiencia

    def imprimirCaracteristicas(self):
        caracteristicas = f"Marca: {self.__marca}\n"
        caracteristicas += f"Voltaje: {self.__voltaje}\n"
        caracteristicas += f"Eficiencia: {self.__eficiencia}\n"
        caracteristicas += f"Precio: ${self.__precio}\n"
        return caracteristicas
