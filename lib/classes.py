class estudiante:
    def __init__(self, matricula, nombre, apellido, edad, calif1=None, calif2=None, calif3=None, calif4=None, calif5=None, promedio=None):
        self.matricula = matricula
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
        self.calif1 = calif1
        self.calif2 = calif2
        self.calif3 = calif3
        self.calif4 = calif4
        self.calif5 = calif5
        self.promedy = promedio
        pass
    
    def setcalif1(self, calif1):
        self.calif1 = calif1
        return 0
    
    def setcalif2(self, calif2):
        self.calif2 = calif2
        return 0
    
    def setcalif3(self, calif3):
        self.calif3 = calif3
        return 0
    
    def setcalif4(self, calif4):
        self.calif4 = calif4
        return 0
    
    def setcalif5(self, calif5):
        self.calif5 = calif5
        return 0

    def calculatepromedio(self):
        if self.promedy == 1:
            try:
                self.promedy = ((self.calif1 + self.calif2 + self.calif3 + self.calif4 + self.calif5)/5)
            except ZeroDivisionError:
                print("¿¡¿¡¿Acaso quieres que colapse el universo al dividir entre 0?!?!?")
            except TypeError:
                print("No puedes dividir Strings entre Números")
            except Exception as e:
                print(f"Error desconocido: {e} ")
            return ((self.calif1 + self.calif2 + self.calif3 + self.calif4 + self.calif5)/5)
        elif self.promedy == 2:
           return f"Promedio"
       
    def __str__(self):
        return f"|{self.matricula}| |{self.nombre} {self.apellido}| |{self.edad}|    |{self.calif1}|  |{self.calif2}|  |{self.calif3}|  |{self.calif4}|  |{self.calif5}| |{self.calculatepromedio()}|"
    pass

class estGrad(estudiante):
    def __init__(self, matricula, nombre, apellido, edad, fecha, tesis, calif1=None, calif2=None, calif3=None, calif4=None, calif5=None, promedio=None):
        super().__init__(matricula, nombre, apellido, edad, calif1, calif2, calif3, calif4, calif5, promedio)
        self.fecha = fecha
        self.tesis = tesis
        pass

    def chkGrad(self):
        if self.promedy <=5.9:
            return f"No esta graduado el alumno"
        elif self.promedy >=6.0:
            return f"Graduado con tesis"    

    def __str2__(self):
        pass  f"Nombre completo:{self.nombre} {self.apellido}  Edad:{self.edad}  Matricula:{self.matricula}  Tesis:{self.tesis} - {self.chkGrad()}"