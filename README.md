## **Proyecto - Examen Cultura General.**
*Joanna Nicole Uriostegui Magaña*
*A01711853*

El proyecto consiste en un modelo de examen de preguntas de cultura general el cual tendrá preguntas abiertas, opción múltiple y de completar.

Podrás seleccionar de que tema deseas que sea cada pregunta. El algoritmo tendra un base de 10 preguntas por tema con su respectiva respuesta y el puntaje de la pregunta a la que accedera para mostrar en pantalla si la respuesta dada es correcta o incorrecta. 

**Orden del algoritmo.**
Pregunta = 1
Mientras no se seleccione la opcion 8:
1.-Mostrar menu de tipo de pregunta:
         1-Matemáticas, 2-Inglés, 3-Química, 8-Salir.
   1.1 Pide al usuario escoger una opción.
2. Entra en la categoría y muestra en pantalla una de las preguntas.
   2.1 Espera la respuesta del usuario
3. Verifica si la respuesta a la pregunta es válida y mostrar en pantalla si es correcta o incorrecta. 
4. De acuerdo a la respuesta, le da un valor a la variable valida.
5. La variable r se manda a la función calificación la cual determina los puntos que se obtuvieron.
6. Suma los puntos a la calificación.
7. Pregunta +1

Terminado el ciclo, muestra en pantalla el promedio (calificación/preguntas).

El código se mostrará las veces que el usuario decia mientras no elija la opción 8, por lo que en base a esas preguntas te mostrará tu calificacion en porcentaje. Siempre y cuando no haya ya pasado por el total de preguntas del tema.

**Salida**.
Mostrar calificación y mensaje de felicitación.
