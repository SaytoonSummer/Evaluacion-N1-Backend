# Clases importadas

from Consola import Consola
from Tv import Tv
from Bicicleta import Bicicleta
from Scooter import Scooter


# Obejos incializados y creados con las clases importadas arriba para simular la base de datos y probar la cotización

tvs = []
tv1 = Tv("Samsung", 12, 120000, "A", 55)
tv2 = Tv("Sony", 10, 800000, "B", 42)
tv3 = Tv("Logitech", 10, 800000, "U", 22)
tvs.extend([tv1, tv2, tv3])

consolas = []
consola1 = Consola("PlayStation 5", "Standard", "Sony", 110, 494999, "A")
consola2 = Consola("Nintendo Switch", "Lite", "Nintendo", 100, 294999, "C")
consolas.extend([consola1, consola2])

scooters = []
scooter1 = Scooter("Xiaomi", "36V", 293999, "C", 10.0, "25 km/h", 12)
scooter2 = Scooter("Segway", "48V",
                   499099, "B", 15.0, "30 km/h", 18)
scooters.extend([scooter1, scooter2])

bicicletas = []
bicicleta1 = Bicicleta(12, 12, 493999, "Trek")
bicicleta2 = Bicicleta(12, 18, 499399, "Giant")
bicicletas.extend([bicicleta1, bicicleta2])

# Funciones para validar de que el usuario ingrese un entero y no se rompa el programa


def obtener_entero(mensaje):
    while True:
        try:
            valor = int(input(f"Ingrese {mensaje}: "))
            return valor
        except ValueError:
            print("Por favor, ingresa un número entero válido.")


def obtener_float(mensaje):
    while True:
        try:
            valor = float(input(f"Ingrese {mensaje}: "))
            return valor
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Bloque de registro de productos para despues crear en sí el objeto con las clases para su posterior guardado en listas, simulando la BD, aparte de su posterior cotización


def registrar_tv():
    print("\n--- Registro de TV ---")
    marca = input("Marca: ")
    voltaje = obtener_entero("Voltaje")
    precio = obtener_float("Precio")
    eficiencia = input("Eficiencia (A/B/C/D/E/F): ")
    tamaño = obtener_float("Tamaño (pulgadas) ")
    tv = Tv(marca, voltaje, precio, eficiencia, tamaño)

    tvs.append(tv)

    print("TV registrado con éxito.\n")
    print(tv.imprimirCaracteristicas())


def registrar_consola():
    print("\n--- Registro de Consola ---")
    nombre = input("Nombre de la Consola: ")
    version = input("Versión: ")
    marca = input("Marca: ")
    voltaje = obtener_entero("Voltaje")
    precio = obtener_float("Precio")
    eficiencia = input("Eficiencia (A/B/C/D/E/F): ")

    consola = Consola(nombre, version, marca, voltaje, precio, eficiencia)
    consolas.append(consola)

    print("Consola registrada con éxito.\n")
    print(consola.imprimirCaracteristicas())


def registrar_scooter():
    print("\n--- Registro de Scooter ---")
    marca = input("Marca: ")
    voltaje = obtener_entero("Voltaje")
    precio = obtener_float("Precio")
    eficiencia = input("Eficiencia (A/B/C/D/E/F): ")
    aro = obtener_float("Aro (pulgadas)")
    velocidad = obtener_entero("Velocidad (km/h)")
    peso = obtener_float("Peso (kg)")

    scooter = Scooter(marca, voltaje, precio, eficiencia, aro, velocidad, peso)

    scooters.append(scooter)

    print("Scooter registrado con éxito.\n")
    print(scooter.imprimirCaracteristicas())


def registrar_bicicleta():
    print("\n--- Registro de Bicicleta ---")
    marca = input("Marca: ")
    aro = obtener_float("Aro (pulgadas)")
    peso = obtener_float("Peso (kg)")
    precio = obtener_float("Precio")

    bicicleta = Bicicleta(aro, peso, precio, marca)

    bicicletas.append(bicicleta)

    print("Bicicleta registrada con éxito.\n")
    print(bicicleta.imprimirCaracteristicas())

# Bloque de cotización de productos


def cotizar_tvs():
    if not tvs:
        print("No hay TVs registradas para cotizar.")
    else:
        print("\n--- Cotización de TVs ---")
        nproducto = 1
        for tv in tvs:
            print(F"TV N°{nproducto} {tv.get_marca()}")
            nproducto += 1
        opcion = obtener_entero("el número del producto que desea cotizar")
        nproducto = 1
        print("\n")
        for tv in tvs:
            if nproducto == opcion:
                precio_original = tv.get_precio()
                print(F"Producto N°{nproducto}")
                print(tv.imprimirCaracteristicas())
                descuento = tv.calcularDescuento()
                precio_con_descuento = precio_original - \
                    (descuento * precio_original)
                print(
                    f"Valor total luego del descuento: ${precio_con_descuento}\n")
                break
            else:
                nproducto += 1


def cotizar_consolas():
    if not consolas:
        print("No hay consolas registradas para cotizar.")
    else:
        print("\n--- Cotización de Consolas ---")
        nproducto = 1
        for consola in consolas:
            print(F"Consola N°{nproducto} {consola.get_marca()}")
            nproducto += 1
        opcion = obtener_entero("el número del producto que desea cotizar")
        nproducto = 1
        print("\n")
        for consola in consolas:
            if nproducto == opcion:
                precio_original = consola.get_precio()
                print(F"Producto N°{nproducto}")
                print(consola.imprimirCaracteristicas())
                descuento = consola.calcularDescuento()
                precio_con_descuento = precio_original - \
                    (descuento * precio_original)
                print(
                    f"Valor total luego del descuento: ${precio_con_descuento}\n")
                break
            else:
                nproducto += 1


def cotizar_scooters():
    if not scooters:
        print("No hay Scooters registrados para cotizar.")
    else:
        print("\n--- Cotización de Scooters ---")
        nproducto = 1
        for scooter in scooters:
            print(f"Scooter N°{nproducto} {scooter.get_marca()}")
            nproducto += 1
        opcion = obtener_entero("el número del producto que desea cotizar")
        nproducto = 1
        print("\n")
        for scooter in scooters:
            if nproducto == opcion:
                precio_original = scooter.get_precio()
                print(f"Producto N°{nproducto}")
                print(scooter.imprimirCaracteristicas())
                descuento = scooter.calcular_descuento()
                costo_despacho = scooter.calcularDespacho()
                precio_con_descuento = precio_original - \
                    descuento + costo_despacho
                print(f"Costo de despacho: ${costo_despacho}")
                print(
                    f"Valor total luego del descuento y despacho: ${precio_con_descuento}\n")
                break
            else:
                nproducto += 1


def cotizar_bicicletas():
    if not bicicletas:
        print("No hay bicicletas registradas para cotizar.")
    else:
        print("\n--- Cotización de Bicicletas ---")
        nproducto = 1
        for bicicleta in bicicletas:
            print(F"Bicicleta N°{nproducto} {bicicleta.get_marca()}")
            nproducto += 1
        opcion = obtener_entero("el número del producto que desea cotizar")
        nproducto = 1
        print("\n")
        for bicicleta in bicicletas:
            if nproducto == opcion:
                precio_original = bicicleta.get_precio()
                print(F"Producto N°{nproducto}")
                print(bicicleta.imprimirCaracteristicas())
                costo_despacho = bicicleta.calcularDespacho()
                precio_total = precio_original + costo_despacho
                print(f"Costo de despacho: ${costo_despacho}")
                print(
                    f"Valor total luego del despacho: ${precio_total}\n")
                break
            else:
                nproducto += 1

# Menú sencillo y de facil uso, creado en base a un ciclo while


def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar TV")
        print("2. Registrar Consola")
        print("3. Registrar Scooter")
        print("4. Registrar Bicicleta")
        print("5. Cotizar TVs")
        print("6. Cotizar Consolas")
        print("7. Cotizar Scooters")
        print("8. Cotizar Bicicletas")
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_tv()
        elif opcion == "2":
            registrar_consola()
        elif opcion == "3":
            registrar_scooter()
        elif opcion == "4":
            registrar_bicicleta()
        elif opcion == "5":
            cotizar_tvs()
        elif opcion == "6":
            cotizar_consolas()
        elif opcion == "7":
            cotizar_scooters()
        elif opcion == "8":
            cotizar_bicicletas()
        elif opcion == "9":
            print("Ha salido del menú. Que tenga un buen día.")
            break
        else:
            print("Opción no válida. Introduce un número del 1 al 9.")


menu()
