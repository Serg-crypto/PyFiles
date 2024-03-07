import random
import pickle

class Vehiculo(object):
    """Clase para crear objetos que representan Vehiculos """

    def __init__(self, code, marca, modelo, motor, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__motor = motor
        self.__precio = precio
        self.__code = code

    def __str__(self):
        return "\nDatos del Vehiculo:\ncode: {}\nmarca: {}\nmodelo: {}\nmotor: {}\nprecio: ${}".format(
            self.__code, self.__marca, self.__modelo, self.__motor, self.__precio)
    
    def obtener_code(self):
        """ Sirve para obtener el código que se usa a la hora de eliminar un determinado elemento del inventario """
        return self.__code


def guardar_lista_vehiculos(lista_vehiculos):
    """ Función para guardar la lista de vehículos en un archivo """
    with open('inventario_vehiculos.pickle', 'wb') as archivo:
        pickle.dump(lista_vehiculos, archivo)


def cargar_lista_vehiculos():
    """ Función para cargar la lista de vehículos desde un archivo """
    try:
        with open('inventario_vehiculos.pickle', 'rb') as archivo:
            return pickle.load(archivo)
    except FileNotFoundError:
        return []


def agregar_vehiculo():
    """ Función para crear instancias de la clase Vehiculo """
    cantidad_digitos = int(input("Para poder registrar el vehiculo es necesario indicar la cantidad de numeros que deseas que se asigne al nombre del vehiculo: "))
    nombre_vehiculo = input("Escribe la marca del vehiculo: ")
    marca_vehiculo = nombre_vehiculo
    modelo_vehiculo = input("Escribe el modelo del vehiculo: ")
    motor_vehiculo = input("Indica motor con el que cuenta del vehiculo (ejemplo: L4, V6): ")
    precio_vehiculo = float(input("Escribe el precio del vehiculo: "))
    digitos = [str(random.randrange(1, 9)) for x in range(cantidad_digitos)]
    digitos = "".join(digitos)
    nombre_objeto = nombre_vehiculo + digitos
    codigo = nombre_objeto
    print(f'El vehiculo se ha registrado exitosamente con el nombre: {nombre_objeto}')
    nombre_objeto = Vehiculo(codigo, marca_vehiculo, modelo_vehiculo, motor_vehiculo, precio_vehiculo)

    # Cargar la lista de vehículos
    lista_vehiculos = cargar_lista_vehiculos()
    # Agregar el nuevo vehículo a la lista
    lista_vehiculos.append(nombre_objeto)
    # Guardar la lista de vehículos actualizada
    guardar_lista_vehiculos(lista_vehiculos)



def mostrar_inventario_actual():
    try:
        with open('inventario_vehiculos.pickle', 'rb') as archivo:
            vehiculos = pickle.load(archivo)
        
        if not vehiculos:
            print("El inventario está vacío")

        for vehiculo in vehiculos:
            print(vehiculo)

    except FileNotFoundError:
        print("No se ha encontrado el inventario")
   
        


def eliminar_vehiculo(codigo):
    """ Función para eliminar un vehículo de la lista por su código """
    # Cargar la lista de vehículos
    lista_vehiculos = cargar_lista_vehiculos()
    # Crear una nueva lista excluyendo el vehículo con el código proporcionado
    lista_actualizada = [vehiculo for vehiculo in lista_vehiculos if vehiculo.obtener_code() != codigo]
    #Guardar la lista actualizada en el archivo
    guardar_lista_vehiculos(lista_actualizada)
    print(f'Vehículo con código {codigo} eliminado correctamente.')





print("Bienvenido!")
opcion = input("Si deseas ver el inventario actual escribe: 1\nSi deseas agregar un vehiculo escribe: 2\nSi deseas eliminar un vehiculo escribe: 3\n: ")
if opcion == "1":
    print("-"*15, "Inventario", "-"*15)
    mostrar_inventario_actual()
    print("-"*42)

elif opcion == "2":
    agregar_vehiculo()
    print("-"*60)

elif opcion == "3":
    identificador = input("Escribe el codigo identificador del vehiculo que deseas eliminar: ")
    eliminar_vehiculo(identificador)

else:
    print("La opción seleccionada no está disponible")

print("Hasta luego!")





