class Libro:
    def __init__(self,titulo,autor,año,codigoU):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.codigoU = codigoU

        def mostrarL(self):
            return (f"CODIGO: {codigo} - TITULO: {titulo} - AUTOR {autor} - AÑO: {año}")



class Usuario:
    def __init__(self,carnet,nombre,carrera):
        self.carnet = carnet
        self.nombre = nombre
        self.carrera = carrera

        def mostrarU(self):
            return (f"CARNET: {carnet} - NOMBRE: {nombre} - CARRERA: {carrera}")


