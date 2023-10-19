import random
#El módulo random. (n.d.). 
#https://python-para-impacientes.blogspot.com/2015/09/el-modulo-random.html

#Funcion que imprime el menu
def menu():
    print("Instrucciones: ")
    print("Selecciona el número del tema del") 
    print("que desees que sea tu pregunta.\n")
    print("         -MENU-\n")
    print(" 1.-Matematicas.\n")
    print(" 2.-Inglés.\n")
    print(" 3.-Quimica.\n")
    print("             8.-Salir.\n")

#funcion para calificar
def calificar(valida, puntos, calificacion):
    #verifica si la pregunta fue correcta.
    if(valida == 1):
        #Revisa el puntaje que le corresponde a la pregunta
        if(puntos == 1):
            calificacion += 8
        elif(puntos == 2):
            calificacion += 10
        elif(puntos == 3):
            calificacion += 15
    #devuelve la calificacion
    return calificacion

#para calcular el promedio
def promedio(calificacion, preguntas):
    #realiza la operacion para calcular el promedio
    return calificacion/preguntas

#funcion que checa que la pregunta no haya sido previemente mostrada
def verificar(num, past):
    for e in past:
        if e == num:
            repetido = 'si'
            #devuelve si o no
            return repetido
    repetido = 'no'
    #agrega el numero a la lista de preguntas pasadas
    past.append(num)
    return repetido

#variables
opcion = 1
calificacion = 0
preguntas = 0
puntos = 0
correcta = ""
respuesta = ""

#listas para verificar que las preguntas no se repitan
preguntas_pasadas_mate = []
preguntas_pasadas_quimica = []
preguntas_pasadas_ingles = []

#preguntas y respuestas
mate = [
    ['¿Nombre el único número primo par?: ', '2', '1'],
    ['¿Cómo se llama también el perímetro de un círculo?: ',
     'circunferencia', '1'],
    ['52 dividido por cuatro es igual a ¿cuánto?: ', '13', '1'],
    ['¿Cuántos segundos hay en un día?: ', '86,400', '2'],
    ['¿Cuántos milímetros hay en un litro?: ', '1000', '1'],

    ['¿Cuál es el cuadrado de 16?: ', '256', '1'],
    ['¿Qué es Pi?:\n a) racional\n  b) irracional\n ', 'b', '1'],
    ['Despeja x de: 9x=108. ', '12', '2'],
    ["""¿Quién es el padre de las matemáticas?:\n
    a) Pitágoras\n b)Tales \n c)Arquímedes\n""", 'c', '3'],
    ['¿Qué número es igual a 334*7+335?: ', '2673', '2']
]
    
quimica = [
    ["""La materia es: \n a) Todo lo que ocupa un lugar en el espacio.\n
     b) Todo lo que refleja.\n c)La transferencia de energia entre cuerpos.
     \n""", 'a', '2'],
    ['¿Cuántos elementos químicos hay?: ','118','1'],
    ['¿Qué gas llevan los refrescos?: ','co2','3'],
    ["""¿Cuáles son las moléculas orgánicas que actúan como catalizadores 
     de reacciones químicas?: """,'enzimas','2'],
    ['¿Qué tipo de sólido es el vidrio?:\n a)amorfo.\n b)cristalino.\n',
     'a','2'],

    ['Cómo es la carga del protón?:\na)Positiva.\nb)Negativa.\nc)Neutrón.\n',
     'a','1'],
    ["""Los isotopos son átomos que tienen el mismo número de protones pero
     diferente numero de ...""",'neutrones','1'],
    ['Un catión ha:\n a)Perdido electrones.\nb)Ganado electrones.\n','b','2'],
    ['¿Cuál es el número atómico del sodio?: a)31\n b)11\n c)52\n','b','1'],
    ["""¿Cuál es el enlace más fuerte?:\n a)Enlace covalente .\n
     b)Enlace metálico.\nc)Enlace iónico\n""",'c','2']
]

ingles = [
    ["""Chinese is probably the ___________ language in the world.\n
     a)most difficult.\n b)difficulter.\n c)difficulty.\n """, 'a', '2'],
    ["""My brother is the _________ person I know:\n a)friendliest\n
     b) more friendly.\n c)friendly\n """, 'a', '2'],
    ["""Robert is _________ in our class.\n a)the beautifuler.\n
     b)the most beautiful.\n c)beautifulest.\n """, 'b', '2'],
    ["""The past tense of work is: """, 'worked', '1'],
    ["""Jack didn't _____ up late last night:""", 'get', '1'],

    ['That movie was so sad, i : ', 'cried', '1'],
    ['Your sister speaks spanish, __________?:  ', 'doesnt she', '3'],
    ['I would love to be famouse, ____________ ?: ', 'wouldnt you', '3'],
    ["There aren't _____ books in Sonia's living room. ", 'any', '2'],
    ['There ____ a wonderful view of the mountains from here. ', 'is', '1']
]

#while para repetir el codigo
while(opcion!=8 and preguntas<30):
    #mostrar menu y pedir al usuario el tema deseado
    menu()
    opcion = float(input("\nSelecciona la opcion deseada: "))

    #entrar a la pregunta segun el tema
    if(opcion == 1):
        #checar que no se haya acabado la base de preguntas
        if(len(preguntas_pasadas_mate) == 10):
            print("Has contestado ya todas las preguntas de la materia,")
            print(" elige otro.")
        else :
            #recordar las instrucciones
            print("Instrucciones: ")
            print("Recuerda que tu respuesta debe estar en minúsculas,")
            print("y si es una cantidad escrita con números.\n")

            print("Has seleccionado: MATEMATICAS\n Pregunta :")#indica el tema
            print(preguntas+1)# y la pregunta

            #generar numero aleatorio para pregunta al azar sin que se repita
            repetido = 'si'
            while repetido == 'si':
                num = random.randint(0, 9)
                repetido = verificar(num, preguntas_pasadas_mate)

            #toma de la matriz la pregunta,
            #respuesta y puntaje
            respuesta = input(mate[num][0])
            correcta = mate[num][1]
            puntos = int(mate[num][2]) #pasar de cadena a entero

            #verifica si la respuesta es correcta
            if(respuesta == correcta):
                print("Correcta!")
                valida = 1
            else:
                print("Incorrecta")
                valida = 0
            print(" ")#para separar

            #suma a calificacion los puntos adecuados
            calificacion = calificar(valida, puntos, calificacion)
            #para contarbilizar las preguntas realizadas
            preguntas += 1
    if(opcion == 2):
        #checar que no se haya acabado la base de preguntas
        if(len(preguntas_pasadas_ingles) == 10):
            print("Has contestado ya todas las preguntas de la materia,")
            print(" elige otro.")
        else :
            #recordar instrucciones
            print("Instrucciones: ")
            print("Recuerda que tu respuesta debe estar en minúsculas,")
            print("y si es una cantidad escrita con números.\n")
            print("No pongas acentos ni apóstrofes, solo escribelo junto,")
            print("y cuando se necesiste con espacio.\n")

            print("Has seleccionado: INGLÉS\n Pregunta :")#indica el rema
            print(preguntas+1)#y pregunta 

            #generar numero aleatorio para pregunta al azar sin que se repita
            repetido = 'si'
            while repetido == 'si':
                num = random.randint(0, 9)
                repetido = verificar(num, preguntas_pasadas_ingles)

            #toma de la matriz la pregunta,
            #respuesta y puntaje
            respuesta = input(ingles[num][0])
            correcta = ingles[num][1]
            puntos = int(ingles[num][2]) #pasar de cadena a entero

            #verifica si la respuesta es correcta
            if(respuesta == correcta):
                print("Correcta!")
                valida = 1
            else:
                print("Incorrecta")
                valida = 0
            print(" ")#para separar

            #suma a calificacion los puntos adecuados
            calificacion = calificar(valida, puntos, calificacion)
            #para contarbilizar las preguntas realizadas
            preguntas += 1
    if(opcion == 3):
        #checar que no se haya acabado la base de preguntas
        if(len(preguntas_pasadas_quimica) == 10):
            print("Has contestado ya todas las preguntas de la materia,")
            print("elige otro.")
        else :
            #recordar las instrucciones
            print("Instrucciones: ")
            print("Recuerda que tu respuesta debe estar en minúsculas,")
            print("y si es una cantidad escrita con números.\n")

            print("Has seleccionado: QUIMICA\n Pregunta :")#indica el tema
            print(preguntas+1)#y pregunta

            #generar numero aleatorio para pregunta al azar sin que se repida
            repetido = 'si'
            while repetido == 'si':
                num = random.randint(0, 9)
                repetido = verificar(num, preguntas_pasadas_quimica)

            #toma de la matriz la pregunta,
            #respuesta y puntaje
            respuesta = input(quimica[num][0])
            correcta = quimica[num][1]
            puntos = int(quimica[num][2]) #pasar de cadena a entero

            #verifica si la respuesta es correcta
            if(respuesta == correcta):
                print("Correcta!")
                valida = 1
            else:
                print("Incorrecta")
                valida = 0
            print(" ")#para separar

            #suma a calificacion los puntos adecuados
            calificacion = calificar(valida, puntos, calificacion)
            #para contarbilizar las preguntas realizadas
            preguntas += 1

#calcula el promedio obtenido
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