class estudiante:
    def __init__(self, matricula, nombre, apellido, edad):
        self.matricula = matricula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        pass
    
    def setCalif(self, calificacion):
        self.califcaciones.append(calificacion)
        pass
    
    def __str__(self):
        return f"|{self.matricula}| |{self.nombre} {self.apellido}| |{self.apellido}| |{self.edad}|"
    pass

class estGrad(estudiante):
    def __init__(self, matricula, nombre, apellido, edad, fecha, tesis):
        super().__init__(matricula, nombre, apellido, edad)
        self.fecha = fecha
        self.tesis = tesis
        pass

    def chkGrad(self):
        pass
    pass