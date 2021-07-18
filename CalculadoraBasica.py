import sys
resultado = 0
num1 = 0
num2 = 0
continuar = True
while continuar == True:
    print("""
            ¡CALCULADORA BASICA USANDO GIT! 
""")
    print()
    opcion = int(input("""
            Operaciones disponibles:

            1) Suma
            2) Resta

            Otras operaciones:

            0)Salir
            
            ¿Que opcion deseas escoger? Escribe el numero correspondiente a la accion a realizar: """))
    print()

    if opcion == 1:
        num1 = int(input("Digite el primer numero: "))
        print()
        num2 = int(input("Digite el segundo numero: "))
        print()
        resultado = num1 + num2
        print("Su resultado es: " + str(resultado))

    elif opcion == 2:
        num1 = int(input("Digite el primer numero: "))
        print()
        num2 = int(input("Digite el segundo numero: "))
        print()
        resultado = num1 - num2
        print("Su resultado es: " + str(resultado))

    elif opcion == 0:
        sys.exit()