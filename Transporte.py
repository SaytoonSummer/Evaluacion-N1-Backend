# Clase padre Transporte, la cual solo va a heredar a Scooter y Bicicleta

class Transporte:

    def __init__(self):
        self.__COSTODESPACHOBASE = 4000

    def get_despacho(self):
        return self.__COSTODESPACHOBASE
