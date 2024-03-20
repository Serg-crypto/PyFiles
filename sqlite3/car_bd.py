import sqlite3




def crear_base():
    """ Función para crear una base de datos que va a contener las categorias de vehiculos disponibles """
    conexion = sqlite3.connect("vehiculos.db")
    cursor = conexion.cursor()

    try:
        cursor.execute(''' CREATE TABLE IF NOT EXISTS categoria(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla de categoría ya existe")

    else:
        print("Se ha creado exitosamente la tabla de categorías")



    try: 
        cursor.execute('''CREATE TABLE IF NOT EXISTS vehiculo(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre VARCHAR(100) UNIQUE NOT NULL,
                       categoria_id INTEGER NOT NULL,
                       FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
        
    except sqlite3.OperationalError:
        print("La tabla con el nombre vehiculos ya existe")
    
    else:
        print("Se ha creado exitosamente la tabla de vehiculos")


    conexion.close()






def agregar_categoria():
    nombre_categoria = input("Escribe el nombre de la categoría que deseas agregar: ")
    conexion = sqlite3.connect("vehiculos.db")
    cursor = conexion.cursor()
    # Agrega una categoria con un determinado nombre
    try:
        cursor.execute("INSERT INTO categoria (nombre) VALUES (?)", (nombre_categoria,))

    except sqlite3.IntegrityError:
        print("La categoría {} ya existe en la base".format(nombre_categoria)) 


    else:
        print("La categoría ha sido agregada exitosamente")


    conexion.commit()
    conexion.close()



def agregar_vehiculo():
    """Funcion para agregar un vehiculo a una categoría"""    
    conexion = sqlite3.connect("vehiculos.db")
    cursor = conexion.cursor()
    # Selecciona todas las categorías existentes para que el usuario pueda indicar a que categoría desea ingresar el vehiculo
    categorias_disponibles = cursor.execute(" SELECT * FROM categoria ").fetchall()
    print("Estas son las categorías disponibles: ")
    for categ in categorias_disponibles:
        print("ID -> ",categ[0]," Categoria ->", categ[1])

    # El usuario indica la categoría a la que desea agregar el vehiculo y el nombre clave del mismo
    cat_vehiculo    = int(input("Escribe el ID de la categoría a la que pertenece el vehiculo que deseas agregar: "))
    nombre_vehiculo = input("Escribe el nombre clave del vehiculo que deseas agregar: ")
    # Intenta agregar un vehiculo a la tabla usando los parametros dados por el usuario
    try:
        cursor.execute("INSERT INTO vehiculo (nombre, categoria_id) VALUES (?, ?)", (nombre_vehiculo, cat_vehiculo))

    except sqlite3.IntegrityError:
        print("El vehiculo {} ya está registrado".format(nombre_vehiculo))
    else:
        print("El vehiculo ha sido registrado correctamente.")
    

    conexion.commit()
    conexion.close()



def remover_vehiculo():
    """Funcion para eliminar un vehiculo a una categoría"""    
    conexion = sqlite3.connect("vehiculos.db")
    cursor = conexion.cursor()

    id_vehiculo = input("Escribe el id del vehiculo que deseas eliminar de la base: ")

    try:
        cursor.execute("DELETE FROM vehiculo WHERE id = ?", (id_vehiculo,))

        # para verificar si se ha eliminado algún vehículo. 
        # Si rowcount es 0, significa que no se eliminó ningún vehículo y levantamos una excepción 
        if cursor.rowcount == 0:
            raise sqlite3.OperationalError("No se encontró un vehiculo con el id: {}".format(id_vehiculo))
        else:
            print("El vehiculo ha sido eliminado correctamente.")

    except sqlite3.OperationalError as e:
        print(e)


    conexion.commit()
    conexion.close()






# Llamada a la función para crear la base de datos en caso de que exista
#crear_base()
        


# Funcionamiento del programa mediante un menu principal con distintas opciones        
while True:
    print("\n")
    print("Bienvenido al gestor de vehiculos!")
    opcion = int(input("Si deseas agregar una categoría escribe un'1'\nSi deseas agregar un vehiculo escribe un'2'\nSi deseas eliminar un vehiculo escribe '3'\nSi deseas salir de este menu escribe '4'\n--> "))

    if opcion == 1:
        agregar_categoria()
    elif opcion == 2:
        agregar_vehiculo()
    elif opcion == 3:
        remover_vehiculo()
    else:
        print("Bye!")
        break