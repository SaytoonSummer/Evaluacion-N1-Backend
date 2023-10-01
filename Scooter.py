# La clase hija mas compleja de todas, ya que hereda de dos padres: Transporte y Tecnologia, teniendo que tomar en cuenta su valor por despacho, y descuento por eficienca si es que se da el caso

from Tecnologia import Tecnologia
from Transporte import Transporte


class Scooter(Tecnologia, Transporte):
    def __init__(self, marca, voltaje, precio, eficiencia, aro, velocidad, peso):
        Tecnologia.__init__(self, marca, voltaje, precio, eficiencia)
        Transporte.__init__(self)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso

    def get_aro(self):
        return self.__aro

    def set_aro(self, aro):
        self.__aro = aro

    def get_velocidad(self):
        return self.__velocidad

    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def calcularDespacho(self):
        costo_despacho = self.get_despacho() + \
            self.__peso * self.valor_por_kilogramo()
        return costo_despacho

    def valor_por_kilogramo(self):
        return 300

    def imprimirCaracteristicas(self):
        print("Características del Scooter:")
        caracteristicas = super().imprimirCaracteristicas()
        caracteristicas += f"Aro: {self.__aro}\n"
        caracteristicas += f"Velocidad: {self.__velocidad} km/h\n"
        caracteristicas += f"Peso: {self.__peso} kg\n"
        return caracteristicas
