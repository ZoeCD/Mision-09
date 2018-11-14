#Zoe Caballero Dominguez A01747247
#Mision 09: diferentes funciones utilizando listas.


# Crea una nueva lista con solo los valores pares de la lista enviada como parámetros
def extraerPares(lista):
    nuevaLista = []

    for dato in lista:
        if dato%2 == 0:
            nuevaLista.append(dato)

    return nuevaLista


# Crea una nueva lista de los elementos que son mayores a un elemento previo.
def extraerMayoresPrevio(lista):
    nuevaLista = []

    for k in range (1,len(lista)):
        if lista[k] > lista[k-1]:
            nuevaLista.append(lista[k])

    return nuevaLista


# Crea una nueva lista cambiando de lugar las parejas de una lista.
def intercambiarParejas(lista):
    listaIndexNones = lista[1::2]
    listaIndexPares = lista[0::2]
    listaNueva =[]

    for n in range(len(lista)//2):
        listaNueva.append(listaIndexNones[n])
        listaNueva.append(listaIndexPares[n])

    if len(lista)%2 == 1:
        listaNueva.append(lista[len(lista)-1])

    return listaNueva


#Modifica la lista original intercambiando de lugar el valor meyor y el menor
def intercambiarMM(lista):

    if len(lista) == 0:
        pass
    else:
        minimo = min(lista)
        maximo = max(lista)

        indexMin = lista.index(minimo)
        indexMax = lista.index(maximo)

        lista[indexMin] = maximo
        lista[indexMax] = minimo


#Regresa el promedio centro de los valores dados por una lista
def promediarCentro(lista):

    if len(lista) <= 2:
        return 0
    else:
        listaNueva = lista.copy()
        listaNueva.remove(min(listaNueva))
        listaNueva.remove(max(listaNueva))
        promedio = sum(listaNueva)//len(listaNueva)

        return promedio


#Regresa una dupla con la media y desviación estándar de los elementos de la lista
def calcularEstadistica(lista):

    if len(lista) == 0:
        return (0,0)
    elif len(lista) == 1:
        return(lista[0], 0)
    else:
        media = sum(lista)/len(lista)
        distanciaMedia = []

        for dato in lista:
            diferenciaCuadrado = (dato - media)**2
            distanciaMedia.append(diferenciaCuadrado)

        desviacion = (sum(distanciaMedia)/(len(lista)-1))**0.5

        return (media,desviacion)


#Calcula la suma de los elementos de una lista, excepto si el valor es 13 o está junto a uno.
def calcularSuma(lista):
    suma = 0

    if len(lista) == 1 and lista[0]!=13:
        suma = lista[0]
    else:
        for k in range(len(lista)):
            anterior = k-1
            posterior = k+1

            if k == 0:
                if lista[k] != 13 and lista[posterior]!=13:
                    suma += lista[k]

            elif k == len(lista)-1:
                if lista[k] != 13 and lista[anterior] != 13:
                    suma+=lista[k]

            elif lista[k] !=13 and lista[anterior] != 13 and lista[posterior] != 13:
                suma+=lista[k]

    return suma

#Función main con pruebas de las fucniones
def main():

    #Listas para pruebas:
    listaVacia = []
    lista1 = [1,2,3,2,4,60,5,8,3,22,44,55]
    lista2 = [5,7,3]
    lista3 = [5,4,3,2]
    lista4 = [1,2,3]
    lista5 = [7]
    lista6 = [5,9,3,22,19,31,10,7]
    lista7 = [70,80,90]
    lista8 = [95,21,73,24,15,69,71,80,49,100,85]
    lista9 = [20,55,30,5,55,5]
    lista10 = [5,9,1,8]
    lista11 = [5,8]
    lista12 = [1,2,3,4,5,6]
    lista13 = [5,2,13,4,1,6,1,8,4,1,5]
    lista14 = [5,2,13,4,1,6,1,8,4,13,1]
    lista15 = [13,49]

    print("Ejercicio 1, valores pares")
    print("De la lista:", lista1, "regresa:", extraerPares(lista1))
    print("De la lista:", lista2, "regresa:", extraerPares(lista2))
    print("De la lista:", listaVacia, "regresa:", extraerPares(listaVacia))
    print("----------------------------------")

    print("Ejercicio 2, valores mayores al elemento previo")
    print("De la lista:", lista1, "regresa:", extraerMayoresPrevio(lista1))
    print("De la lista:", lista3, "regresa:", extraerMayoresPrevio(lista3))
    print("De la lista:", listaVacia, "regresa:", extraerMayoresPrevio(listaVacia))
    print("----------------------------------")

    print("Ejercicio 3, intercambia el lugar de las parejeras")
    print("De la lista:", lista1, "regresa:", intercambiarParejas(lista1))
    print("De la lista:", lista4, "regresa:", intercambiarParejas(lista4))
    print("De la lista:", lista5, "regresa:", intercambiarParejas(lista5))
    print("De la lista:", listaVacia, "regresa:", intercambiarParejas(listaVacia))
    print("----------------------------------")

    print("Ejercicio 4, intercambia el lugar del valor mayor y menor")
    print("A la lista:", lista6)
    intercambiarMM(lista6)
    print("la vuelve:", lista6)
    print("A la lista:", lista4)
    intercambiarMM(lista4)
    print("la vuelve:", lista4)
    print("A la lista:", listaVacia)
    intercambiarMM(listaVacia)
    print("la vuelve:", listaVacia)
    print("----------------------------------")

    print("Ejercicio 5, da el promedio 'centro' de la lista")
    print("De la lista:", lista7, "regresa:", promediarCentro(lista7))
    print("De la lista:", lista8, "regresa:", promediarCentro(lista8))
    print("De la lista:", lista9, "regresa:", promediarCentro(lista9))
    print("De la lista:", lista10, "regresa:", promediarCentro(lista10))
    print("De la lista:", lista11, "regresa:", promediarCentro(lista11))
    print("De la lista:", listaVacia, "regresa:", promediarCentro(listaVacia))
    print("----------------------------------")

    print("Ejercicio 6, calcula la media y desviación estándar")
    print("De la lista:", lista12, "regresa:", calcularEstadistica(lista12))
    print("De la lista:", lista8, "regresa:", calcularEstadistica(lista8))
    print("De la lista:", listaVacia, "regresa:", calcularEstadistica(listaVacia))
    print("----------------------------------")

    print("Ejercicio 7, suma los números que no sean 13 o estén junto a éste")
    print("De la lista:", lista12, "regresa:", calcularSuma(lista12))
    print("De la lista:", lista13, "regresa:", calcularSuma(lista13))
    print("De la lista:", lista14, "regresa:", calcularSuma(lista14))
    print("De la lista:", lista15, "regresa:", calcularSuma(lista15))
    print("De la lista:", listaVacia, "regresa:", calcularSuma(listaVacia))
    print("----------------------------------")


#Llamar a main
main()