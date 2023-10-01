from Tecnologia import Tecnologia


class Tv(Tecnologia):
    def __init__(self, marca, voltaje, precio, eficiencia, tamaño):
        super().__init__(marca, voltaje, precio, eficiencia)
        self.__tamaño = tamaño

    def get_tamaño(self):
        return self.__tamaño

    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño

    def calcularDescuento(self):
        descuento_eficiencia = super().calcular_descuento()
        return descuento_eficiencia

    def imprimirCaracteristicas(self):
        print("Caracteristicas Tv:")
        caracteristicas = super().imprimirCaracteristicas()
        caracteristicas += f"Tamaño: {self.__tamaño} pulgadas\n"
        return caracteristicas
