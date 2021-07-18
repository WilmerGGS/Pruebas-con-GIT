resultado = 0
num1 = 0
num2 = 0
print("""
            ¡CALCULADORA BASICA USANDO GIT! 
""")
print()
opcion = int(input("""
            Operaciones disponibles:

            1) Suma
            2) Resta
            3) Multiplicacion
            4) Division

            Otras operaciones:

            0)Salir
            9)Volver a la calculadora basica
            
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

elif opcion == 3:
    num1 = int(input("Digite el primer numero: "))
    print()
    num2 = int(input("Digite el segundo numero: "))
    print()
    resultado = num1 * num2
    print("Su resultado es: " + str(resultado))

elif opcion == 4:
    num1 = int(input("Digite el primer numero: "))
    print()
    num2 = int(input("Digite el segundo numero: "))
    print()
    resultado = num1 / num2
    print("Su resultado es: " + str(resultado))