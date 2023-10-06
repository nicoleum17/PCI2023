import random

#Funcion que imprime el menu
def menu():
    print("         -MENU-\n")
    print(" 1.-Matematicas.\n")
    print(" 2.-Historia.\n")
    print(" 3.-Quimica.\n")
    print("             8.-Salir.\n")

#funcion para calificar
def calificar(r, p, calificacion):
    #verifica si la pregunta fue correcta.
    if(r == 1):
        #Revisa el puntaje que le corresponde a la pregunta
        if(p == 1):
            calificacion += 8
        elif(p == 2):
            calificacion += 10
        elif(p == 3):
            calificacion += 15
    return calificacion

#para calcular el promedio
def promedio(calificacion, preguntas):
    return calificacion/preguntas

#variables
opcion = 1
calificacion = 0
preguntas = 0
p = 0
correcta = ""
respuesta = ""

#preguntas y respuestas
ma = [
    ['¿Nombre el único número primo par?: ', '2', '1'],
    ['¿Cómo se llama también el perímetro de un círculo?: ', 'circunferencia', '1'],
    ['53 dividido por cuatro es igual a ¿cuánto?: ', '13', '1'],
    ['¿Cuántos segundos hay en un día?: ', '86,400', '2'],
    ['¿Cuántos milímetros hay en un litro?: ', '1000', '1'],
    ['¿Cuál es el cuadrado de 16?: ', '256', '1'],
    ['¿Qué es Pi?:\n a) racional\n  b) irracional\n ', 'b', '1'],
    ['Despeja x de: 9x=108. ', '12', '2'],
    ['¿Quién es el padre de las matemáticas?:\n a) Pitágoras\n b)Tales \n c)Arquímedes\n', 'c', '3'],
    ['¿Qué número es igual a 334*7+335?: ', '2673', '2']
]
    
qui = [
    ['La materia es: \n a) Todo lo que ocupa un lugar en el espacio. \n b) Todo lo que refleja.\n c)La transferencia de energia entre cuerpos. \n', 'a', '2'],
    ['¿Cuántos elementos químicos hay?: ','118','1'],
    ['¿Qué gas llevan los refrescos?: ','co2','3'],
    ['¿Cuáles son las moléculas orgánicas que actúan como catalizadores de reacciones químicas?: ','enzimas','2'],
    ['¿Qué tipo de sólido es el vidrio?:\n a)amorfo.\n b)cristalino.\n','a','2'],

    ['Cómo es la masa del protón?:\n a)Positiva. \n b)Negativa. \n c)Neutrón. \n','a','1'],
    ['Los isotopos son átomos que tienen el mismo número de protones pero diferente numero de ...','neutrones','1'],
    ['Un catión ha:\n a)Perdido electrones.\n b)Ganado electrones.\n','b','2'],
    ['¿Cuál es el número atómico del sodio?: a)31\n b)11\n c)52\n','b','1'],
    ['¿Cuál es el enlace más fuerte?: a)Enlace covalente .\n b)Enlace metálico.\n c)Enlace iónico\n','c','2']
]

#while para repetir el codigo
while(opcion!=8):
    #mostrar menu y pedir al usuario el tema deseado
    menu()
    opcion = float(input("\nSelecciona la opcion deseada: "))

    #entrar a la pregunta segun el tema
    
    if(opcion == 1):
        #escoger al azar una pregunta del tema
        #determinar si la respuesta es correcta r=1
        #mandar r a calificacion
        print("Has seleccionado: MATEMATICAS\n Pregunta :")
        print(preguntas+1)
        #generar numero aleatorio para pregunta al azar
        num = random.randint(0, 9)

        respuesta = input(ma[num][0])
        correcta = ma[num][1]
        p = int(ma[num][2]) #pasar de cadena a entero

        if(respuesta == correcta):
            print("Correcta!")
            r = 1
        else:
            print("Incorrecta")
            r = 0
        calificacion = calificar(r, p, calificacion)
        #para contar las preguntas realizadas
        preguntas += 1
    if(opcion == 3):
        #escoger al azar una pregunta del tema
        #determinar si la respuesta es correcta r=1
        #mandar r a calificacion
        print("Has seleccionado: QUIMICA\n Pregunta :")
        print(preguntas+1)
        #generar numero aleatorio para pregunta al azar
        num = random.randint(0,9)

        respuesta = input(qui[num][0])
        correcta = qui[num][1]
        p = int(ma[num][2]) #pasar de cadena a entero

        if(respuesta == correcta):
            print("Correcta!")
            r = 1
            p = qui[num][2] #mandamos el puntaje de la pregunta
        else:
            print("Incorrecta")
            r = 0
        calificacion = calificar(r, p, calificacion)
        #para contar las preguntas realizadas
        preguntas += 1


resultado = promedio(calificacion, preguntas)

#Determinar el tipo de calificacion que se obtuvo
if(resultado<7):
    print("\n Calificación: ", resultado)
    print("\nIntentalo nuevamente!")
elif(resultado<9):
    print("\n Calificación: ", resultado)
    print("\nBien hecho!")
else:
    print("\n Calificación: ", resultado)
    print("\nFelicidades, lo conseguiste!")