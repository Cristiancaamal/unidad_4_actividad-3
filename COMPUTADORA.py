

#EQUIPO: CRISTIAN CAAMAL, HENRY UICAB, DIANA BALAM
#Importando pyswip para realizar el puente para python que permite consultar prolog
from pyswip import Prolog
prolog = Prolog()
#realizando la consulta en el programa prolog de los hechos
prolog.consult("hechos.pl")
#Imprimiendo el titulo
print("Sistema para la predicción de problemas de software y hardware de una laptop")

r = False
# REALIZANDO LOS CICLOS FOR PARA LAS CONSTRUCCIÓN DEL PROGRAMA, AQUÍ SE EJECUTAN LAS SENTENCIAS MIENTRAS LA CONDICIÓN SEA VERDADERA, AL MOMENTO DE SER FALSA TERMINA EL CICLO
while not r:
    
    #LLAMA E IMPRIME LAS PERSONAS QUE TIENEN PROBLEMAS EN SU EQUIPO
    for valor in prolog.query("reparacion(X,falla)"):
        print (' REQUIERE VERIFICAR EL EQUIPO => ', valor ["X"])
    #MUESTRAS LOS LAS PERSONAS QUE SU EQUIPO REQUIERE UNA REPARACION
    for valor in prolog.query("sinreparacion(X)"):
        print (' REQUIERE REPARACIÓN SU EQUIPO => ', valor ["X"])

     #IMPRIME LAS PERSONAS QUE TIENEN UN DAÑO FISICO EN SU EQUIPO   
    for valor in prolog.query("equipodanado(X,covid)"):
        print (' SU EQUIPO TIENE DAÑOS => ', valor ["X"])
    #IMPRIME LAS PERSONAS QUE NO TIENEN DAÑO FISICO EN SU EQUIPO
    for valor in prolog.query("sindano(X)"):
        print (' SU EQUIPO NO TIENE DAÑOS => ', valor ["X"])
    #LEE EL NOMBRE DE LA PERSONA INGRESADA CON PROBLEMAS DE SOFTWARE
    X= input("----\nPor Software\n----\n Inserta el nombre de la persona ")
    #DICE QUE PROBLEMA TIENE EL EQUIPO POR SOFTWARE
    for valor in prolog.query("tiene("+X+ ", Y)"):
        print (X,' Tiene problemas de  => ', valor ["Y"],"Favor de revisar su equipo con un experto")

    #LEE EL NOMBRE DE LA PERSONA POR PROBLEMAS DE HARDWARE
    X= input("----\nPor hardware\n-----\nInserta el nombre de la persona ")
    #DICE EL PROBLEMA DE HARWARE QUE TIENE
    for valor in prolog.query("error("+X+ ", Y)"):
        print (X,' Daño de  => ', valor ["Y"],"Favor de verificar el equipo")    

    #PRESIONAR 1 0 2 PARA TERMINAR O SEGUIR CON EL PROGRAMA
    e = input('1.-SI  2.-NO\n¿Terminaste con la consulta? ')
    
    #SI SE DETECTA QUE LA ENTRADA ANTERIOR ES 1 IMPRIME EL MENSAJE Y SALE DEL PROGRAMA
    r = e.lower() in ['1']
    if r:
        print("GRACIAS POR USAR EL PROGRAMA")
        
        

