#variables y funciones
libros = {
    'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
    'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
    'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
    'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
    'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
    'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False],
}
prestamos = {
    'L001': [500, 4],
    'L002': [700, 0],
    'L003': [300, 10],
    'L004': [400, 2],
    'L005': [600, 1],
    'L006': [350, 6],
}

def mostrar_menu():
    print ("========== MENÚ PRINCIPAL ==========")
    print("1. Copias por género")
    print("2. Búsqueda de libros por rango de multa")
    print("3. Actualizar multa de libro")
    print("4. Agregar libro")
    print("5. Eliminar libro")
    print("6. salir")

def leer_opcion():
    opcion = (input("ingrese una opcion del menu por su valor numerico: "))

    if opcion.isdigit():
        opcion = int(opcion)

    try:
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("opcion no valida, eliga una entre 1 y 6 por favor")
    except:
        print("opcion no valida, eliga una entre 1 y 6 por favor")

def copias_genero(genero):
    
    for i in libros:
        if genero == libros[i][2]:
            codigo_usar = i
            print(f"El genero {libros[codigo_usar][2]} tiene {prestamos[codigo_usar][1]} copias disponibles")

def buscar_libros_por_rango_multa(val_min, val_max):
    for i in prestamos:
        if val_min <= prestamos[i][0] <= val_max:
            codigo_usar = i
            print(f"El libro {libros[codigo_usar][0]} tiene una multa de ${prestamos[codigo_usar][0]} y {prestamos[codigo_usar][1]} copias disponibles")
    if not any(val_min <= prestamos[i][0] <= val_max for i in prestamos):
        print("No se encontraron libros con multa en ese rango")

def actualizar_multa_libro(codigo, nueva_multa):
    if buscar_codigo(codigo):
        prestamos[codigo][0] = nueva_multa
        print(f"Se ha actualizado la multa del libro {libros[codigo][0]} a ${nueva_multa}")
    else:
        print("El codigo ingresado no existe en el sistema")

def buscar_codigo(codigo):
    if codigo in libros:
        return True
    else:
        return False

def validar_codigo(codigo):
    if codigo in libros:
        print("El codigo ingresado ya existe, por favor ingrese uno diferente")
        return False
    else:
        if codigo == "":
            print("El codigo no puede estar vacío o tener solo espacios")
            return False
        return True

def validar_titulo(titulo):
    if titulo == "":
        print("El titulo no puede estar vacío o tener solo espacios")
        return False
    else:
        return True

def validar_autor(autor):
    if autor == "":
        print("El autor no puede estar vacío o tener solo espacios")
        return False
    else:
        return True

def validar_genero(genero):
    if genero == "":
        print("El genero no puede estar vacío o tener solo espacios")
        return False
    else:
        return True

def validar_año(año):
    if not año.isdigit():
        print("El año debe ser un número entero")
        return False
    else:
        año = int(año)
    if año <= 0:
        print("El año no puede ser negativo o igual a cero")
        return False
    else:
        return True

def validar_editorial(editorial):
    if editorial == "":
        print("La editorial no puede estar vacía o tener solo espacios")
        return False
    else:
        return True

def validar_es_novedad(es_novedad):
    if es_novedad.lower() == "s":
        return True
    elif es_novedad.lower() == "n":
        return False
    else:
        print("Por favor, ingrese 's' para sí o 'n' para no")
        return False

def validar_precio_multa(precio_multa):
    if not precio_multa.isdigit():
        print("El precio de la multa debe ser un número entero")
        return False
    else:
        precio_multa = int(precio_multa)
    if precio_multa <= 0:
        print("El precio de la multa no puede ser negativo o igual a cero")
        return False
    else:
        return True

def validar_copias_disponibles(copias_disponibles):
    if not copias_disponibles.isdigit():
        print("La cantidad de copias disponibles debe ser un número entero")
        return False
    else:
        copias_disponibles = int(copias_disponibles)
    if copias_disponibles <= 0:
        print("La cantidad de copias disponibles no puede ser negativa o igual a cero")
        return False
    else:
        return True

def agregar_libro(N_codigo, titulo, autor, genero, año, editorial, es_novedad, precio_multa, copias_disponibles):
    libros[N_codigo] = [titulo, autor, genero, año, editorial, es_novedad]
    prestamos[N_codigo] = [precio_multa, copias_disponibles]
    print(f"Se ha agregado el libro {titulo} con codigo {N_codigo} al sistema")

def eliminar_libro(codigo):
    if buscar_codigo(codigo):
        del libros[codigo]
        del prestamos[codigo]
        return True
    else:
        return False
#sistema

opcion = 0

while opcion != 6:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        genero = input("ingrese el genero a buscar: ")
        genero = genero.lower()
        copias_genero(genero)
    
    elif opcion == 2:
        val_min = input("ingrese el valor minimo de la multa: ")
        val_max = input("ingrese el valor maximo de la multa: ")
        if val_min.isdigit() and val_max.isdigit():
            val_min = int(val_min)
            val_max = int(val_max)
            if val_min > val_max:
                print("el valor minimo no puede ser mayor al valor maximo, por favor intentelo nuevamente")
            if val_min <= 0 or val_max <= 0:
                print("los valores no pueden ser negativos o iguales a 0, por favor intentelo nuevamente")
            buscar_libros_por_rango_multa(val_min, val_max)
        else:
            print("los valores ingresados no son validos, por favor intentelo nuevamente")
    
    elif opcion == 3:
        codigo = input("ingrese el codigo del libro a actualizar: ")
        codigo = codigo.upper()
        nueva_multa = input("ingrese la nueva multa del libro: ")
        if nueva_multa.isdigit():
            nueva_multa = int(nueva_multa)
            actualizar_multa_libro(codigo, nueva_multa)
        else:
            print("El precio de la multa debe ser un número entero")
    
    elif opcion == 4:
        N_codigo = input("ingrese el codigo del libro a agregar: ")
        N_codigo = N_codigo.upper()
        titulo = input("ingrese el titulo del libro: ")
        autor = input("ingrese el autor del libro: ")
        genero = input("ingrese el genero del libro: ")
        año = input("ingrese el año de publicacion del libro: ")
        editorial = input("ingrese la editorial del libro: ")
        es_novedad = input("el libro es novedad? (s/n): ")
        precio_multa = input("ingrese el precio de la multa del libro: ")
        copias_disponibles = input("ingrese la cantidad de copias disponibles del libro: ")

        validaciones = (validar_codigo(N_codigo) and validar_titulo(titulo) and validar_autor(autor) and validar_genero(genero) and validar_año(año) and validar_editorial(editorial) and validar_es_novedad(es_novedad) and validar_precio_multa(precio_multa) and validar_copias_disponibles(copias_disponibles))
        if validaciones:
            año = int(año)
            precio_multa = int(precio_multa)
            copias_disponibles = int(copias_disponibles)
            agregar_libro(N_codigo, titulo, autor, genero, año, editorial, es_novedad, precio_multa, copias_disponibles)
        else:
            print("no se pudo agregar el libro, por favor intentelo nuevamente")

    elif opcion == 5:
        codigo = input("ingrese el codigo del libro a eliminar: ")
        codigo = codigo.upper()
        if eliminar_libro(codigo):
            print(f"Se ha eliminado el libro con codigo {codigo} del sistema")
        else:
            print("el codigo ingresado no existe en el sistema, por favor intentelo nuevamente")
    
    elif opcion == 6:
        print("programa finalizado")