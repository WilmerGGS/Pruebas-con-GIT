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