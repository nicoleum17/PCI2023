#Funcion que imprime el menu
def menu():
    print("         -MENU-\n")
    print(" 1.-Matematicas.\n")
    print(" 2.-Historia.\n")
    print(" 3.-Quimica.\n")
    print("             8.-Salir.\n")

#funcion para calificar
def calificar(r, calificacion):
    #verifica si la pregunta fue correcta.
    if(r == 1):
        #Revisa el puntaje que le corresponde a la pregunta
        if(p == 1):
            calificacion += 10
        #la pregunta tendrá dos respuestas
        #aqui ve si se respondieron las dos bien
        elif(p == 2):
            calificaion += 7.5
        elif(p == 22):
            calificacion += 15
        #para el caso de 3 respuestas
        elif(p == 3):
            calificacion += 7
        elif(p == 33):
            calificacion += 14
        elif(p == 333):
            calificacion += 20
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
pre_ma=['¿Nombre el único número primo par?: ', '¿Cómo se llama también el perímetro de un círculo?: ', '53 dividido por cuatro es igual a ¿cuanto?: ']
co_ma=['dos', 'circunferencia', '13']

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
        print("Has seleccionado: MATEMATICAS\n")
        print(preguntas+1)
        respuesta = input(pre_ma[2])
        correcta = co_ma[2]
        if(respuesta == correcta):
            print("Correcta!")
            r = 1
            p = 1
        else:
            print("Incorrecta")
            r = 0
        calificacion = calificar(r, calificacion)
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