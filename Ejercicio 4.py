# Matriz de la videoteca
matriz = [
    ["Avatar", 2009, 8.5, "Sci-Fi"],
    ["Dune", 2021, 8.3, "Acción"],
    ["Mario Bros", 2023, 7.1, "Animación"],
    ["Titanic", 1997, 9.0, "Drama"],
    ["Batman", 2022, 8.1, "Acción"],
    ["Interestelar", 2014, 8.7, "Ciencia Ficción"],
    ["Deadpool", 2016, 7.9, "Comedia"]
]

# Función para contar títulos
def contar_titulos(matriz, umbral, año_limite):

    contador = 0

    # Recorrer la matriz
    for pelicula in matriz:

        # pelicula[2] = calificación
        # pelicula[1] = año

        if pelicula[2] >= umbral and pelicula[1] >= año_limite:
            contador += 1

    return contador


# Pedir datos al usuario
umbral = float(input("Ingrese la calificación mínima: "))
año_limite = int(input("Ingrese el año límite: "))

# Llamar la función
resultado = contar_titulos(matriz, umbral, año_limite)

# Mostrar resultado
print("Cantidad de títulos que cumplen:", resultado)