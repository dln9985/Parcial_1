from lib import *
print()

Menu  = estudiante("Matricula","Nombre ","Apellido ", "Edad")
Menu.setcalif1("Cal.1")
Menu.setcalif2("Cal.2")
Menu.setcalif3("Cal.3")
Menu.setcalif4("Cal.4")
Menu.setcalif5("Cal.5")
Menu.calculatepromedio(2)

alum1 = estudiante("601049   ","Zaira   ","Frine   ", "35  ")
alum1.setcalif1(10)
alum1.setcalif2(9)
alum1.setcalif3(8)
alum1.setcalif4(10)
alum1.setcalif5(9)
alum1.calculatepromedio(1)

alum2 = estudiante("100738   ","Victor  ","Garcia  ", "20  ")
alum2.setcalif1(8)
alum2.setcalif2(3)
alum2.setcalif3(4)
alum2.setcalif4(5)
alum2.setcalif5(4)
alum2.calculatepromedio(1)

alum3 = estudiante("100744   ","Diego   ","Lopez   ", "18  ")
alum3.setcalif1(10)
alum3.setcalif2(9)
alum3.setcalif3(8)
alum3.setcalif4(10)
alum3.setcalif5(8)
alum3.calculatepromedio(1)

alum4 = estudiante("100692   ","Evelyn  ","Lopez   ", "20  ")
alum4.setcalif1(10)
alum4.setcalif2(8)
alum4.setcalif3(9)
alum4.setcalif4(5)
alum4.setcalif5(9)
alum4.calculatepromedio(1)

alum5 = estudiante("099999   ","Daniel  ","Rojas   ", "20  ")
alum5.setcalif1(6)
alum5.setcalif2(5)
alum5.setcalif3(4)
alum5.setcalif4(4)
alum5.setcalif5(3)
alum5.calculatepromedio(1)

alum6 = estudiante("100870   ","Maurizio","Rosas   ", "20  ")
alum6.setcalif1(10)
alum6.setcalif2(6)
alum6.setcalif3(10)
alum6.setcalif4(9)
alum6.setcalif5(8)
alum6.calculatepromedio(1)

alum7 = estudiante("100437   ","Annibal ","Villegas", "20  ")
alum7.setcalif1(10)
alum7.setcalif2(5)
alum7.setcalif3(7)
alum7.setcalif4(8)
alum7.setcalif5(10)
alum7.calculatepromedio(1)

print("\t\t\t\t\t CALIFICACIONES \t")
print(Menu)
print("--------------------------------------------------------------------------------------------")
print(alum1)
print(alum2)
print(alum3)
print(alum4)
print(alum5)
print(alum6)
print(alum7)
print()

alum1 = estGrad("Zaira   ","Frine   ", "35  ","601049   ", "por que los cocodrilos muerden?")
alum2 = estGrad("Victor  ","Garcia  ", "20  ","100738   ")
alum3 = estGrad("Diego   ","Lopez   ", "18  ","100744   ", "por que los tiburones muerden?")
alum4 = estGrad("Evelyn  ","Lopez   ", "20  ","100692   ", "por que los perros muerden?")
alum5 = estGrad("Daniel  ","Rojas   ", "20  ","099999   ")
alum6 = estGrad("Maurizio","Rosas   ", "20  ","100870   ", "por que los gatos muerden?")
alum7 = estGrad("Annibal ","Villegas", "20  ","100437   ", "por que los pericos muerden?")

print(alum1)
print(alum2)
print(alum3)
print(alum4)
print(alum5)
print(alum6)
print(alum7)
print()