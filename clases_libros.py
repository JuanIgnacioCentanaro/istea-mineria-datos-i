class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

    def mostrar(self):
        datos = f'Título: {self.titulo}\n Autor: {self.autor}\n Género: {self.genero}\n Puntuación: {self.puntuacion}'
        return datos
        
lista_libros = [Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5),
    Libro("1984", "George Orwell", "Ciencia Ficción", 4.3),
    Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7),
    Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2),
    Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4),
    Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6),
    Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8),
    Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4),
    Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)]      

def agregar_libro():
    titulo = input("Ingrese el título del libro: ").title()
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ").title()
    puntuacion = float(input("Ingrese la puntuación del libro (0-5): "))
    agregado = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(agregado)

def buscar_por_genero():
    gen = input("Género que busca: ").title
    libros_en_gen = [libro.titulo for libro in lista_libros if libro.genero == gen]
    if libros_en_gen:
        print(f"Libros en el género {gen}:") 
    for titulo in libros_en_gen:
        print(f"{titulo}=")  
    else:
        print(f"No se encontraron libros en el género '{gen}'.")

def libro_interes():
    interes = input("Ingrese su género favorito: ").title()
    libros_en_gen = [libro for libro in lista_libros if libro.genero== interes]
    if libros_en_gen:
        mejor_valorado = max(libros_en_gen, key=lambda libro: libro.puntuacion)
        print(f"El libro mejor puntuado en el género '{interes}' es {mejor_valorado.titulo} con una puntuación de {mejor_valorado.puntuacion}.")
    else:
        print(f"No se encontraron libros en el género {interes}.")
    print()


while True:
    print("1 Agregar Libro")
    print("2 Buscar Libros por Género")
    print("3 Recomendar Libro")
    print("4 Salir")
    
    opcion = input("Ingrese el número de la opción deseada: ")
    
    if opcion == '1':
        agregar_libro()
    elif opcion == '2':
        buscar_por_genero()
    elif opcion == '3':
        libro_interes()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.\n")
    
    #agregar_libro() if opcion == '1' else buscar_por_genero() if opcion == '2' \
     #   else libro_interes() if opcion == '3' else print("Chau!") if opcion == '4' else print("Por favor, intente de nuevo.\n")
        
  
        

        
        

