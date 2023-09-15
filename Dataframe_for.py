import pandas as pd
# Crear una tabla con dos columnas, la primera se llamará x  y la segunda se llamará y. Ambas columnas tendrán valores dados por el usuario.
# Convertir la table en una dataframe y filtrar los datos para verificar si entre los datos se encuentra una fila x = 2  y = 5
Valores_Lista = int(input("Indica el numero de filas que deseas: "))
print("---------------------------------------------------------------------")
datos = []
for x in range(0, Valores_Lista):
    listaTemp = []
    datos.append(listaTemp)
    for y in range(2):
        option = input("Si deseas ingresar una cadena de texto escribe 'txt'\nSi desea ingresar un numero, escribe 'num': ").lower()
        print("---------------------------------------------------------------------")
        if option == "txt":
            valor = input("Escribe el valor que deseas agregar: ")
            listaTemp.append(valor)
        else:
            valor = int(input("Escribe el valor que deseas agregar: "))
            listaTemp.append(valor)

points = pd.DataFrame(data=datos, columns=["x","y"])
print(points)

ValoresBuscados = {'x': 2, 'y': 5}
for index, fila in points.iterrows():
    if fila['x'] == ValoresBuscados['x'] and fila['y'] == ValoresBuscados['y']:
        print(f'Los valores buscados {ValoresBuscados} coinciden con los valores de la fila con indice {index}')
    else:
        print(f'Los valores buscados NO coinciden con los valores de la fila con indice {index}')