from Tecnologia import Tecnologia


class Consola(Tecnologia):
    def __init__(self, nombreConsola, version, marca, voltaje, precio, eficiencia):
        super().__init__(marca, voltaje, precio, eficiencia)
        self.__nombreConsola = nombreConsola
        self.__version = version

    def get_nombreConsola(self):
        return self.__nombreConsola

    def set_nombreConsola(self, nombreConsola):
        self.__nombreConsola = nombreConsola

    def get_version(self):
        return self.__version

    def set_version(self, version):
        self.__version = version

    def calcularDescuento(self):
        descuento_eficiencia = super().calcular_descuento()
        descuento_lite = 0

        if "Lite" in self.__version or "lite" in self.__version:
            descuento_lite = 0.05
            print("Obtiene un descuento adicional del 5% por la versión de la consola")

        return descuento_eficiencia + descuento_lite

    def imprimirCaracteristicas(self):
        print("Características de la Consola:")
        caracteristicas = super().imprimirCaracteristicas()
        caracteristicas += f"Nombre de la Consola: {self.__nombreConsola}\n"
        caracteristicas += f"Versión: {self.__version}\n"
        return caracteristicas
