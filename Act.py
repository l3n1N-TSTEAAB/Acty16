class Libro:
    def __init__(self,titulo,autor,año,codigoU):
        self.codigoU = codigoU
        self.titulo = titulo
        self.autor = autor
        self.año = año

        def mostrarL(self):
            return (f"CODIGO: {codigoU} - TITULO: {titulo} - AUTOR {autor} - AÑO: {año}")



class Usuario:
    def __init__(self,carnet,nombre,carrera):
        self.carnet = carnet
        self.nombre = nombre
        self.carrera = carrera

        def mostrarU(self):
            return (f"CARNET: {carnet} - NOMBRE: {nombre} - CARRERA: {carrera}")


def RegistroLibros():
    def __init__(self):
        self.libros = {}

    def AgregarLibro(self):
            codigo = input("Codigo de libro: ")
            if codigo in self.libros:
                print("El libro ya existe.\n")
                return

            titulo = input("titulo del libro: ")
            autor = input("autor del libro: ")
            año = input("año de publicacion: ")

            self.libros[codigo] = Libro(titulo,autor,año)
            print("LIBRO AGREGADO A BIBLIOTECA")
class GestionarPrestamo:
    pass


class Devolucion:
    pass


class DevolucionLibro:
    pass
