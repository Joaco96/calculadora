import funciones_calculadora

def desplegar_menu(a, b):
    """Muestra el menú principal con los valores actuales de A y B."""
    print(f"\nCalculadora")
    print(f"1. Ingresar 1er operando (A={a})")
    print(f"2. Ingresar 2do operando (B={b})")
    print(f"3. Calcular todas las operaciones")
    print(f"4. Informar resultados")
    print(f"5. Salir")

def ingresar_operando(mensaje):
    """Solicita al usuario ingresar un operando.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario.
    
    Returns:
        float: El operando ingresado por el usuario.
    """
    return float(input(mensaje))

def main():
    a = 0
    b = 0
    resultados = {}

    while True:
        desplegar_menu(a, b)
        opcion = input("Seleccionar una opción: ")

        if opcion == '1':
            a = ingresar_operando("Ingrese el 1er operando: ")
        elif opcion == '2':
            b = ingresar_operando("Ingrese el 2do operando: ")
        elif opcion == '3':
            resultados['suma'] = funciones_calculadora.sumar(a, b)
            resultados['resta'] = funciones_calculadora.restar(a, b)
            resultados['division'] = funciones_calculadora.dividir(a, b)
            resultados['multiplicacion'] = funciones_calculadora.multiplicar(a, b)
            resultados['factorial_a'] = funciones_calculadora.calcular_factorial(int(a))
            resultados['factorial_b'] = funciones_calculadora.calcular_factorial(int(b))
        elif opcion == '4':
            if resultados:
                print(f"El resultado de A+B es: {resultados['suma']}")
                print(f"El resultado de A-B es: {resultados['resta']}")
                print(f"El resultado de A/B es: {resultados['division']}")
                print(f"El resultado de A*B es: {resultados['multiplicacion']}")
                print(f"El factorial de A es: {resultados['factorial_a']} y el factorial de B es: {resultados['factorial_b']}")
            else:
                print("Primero debe calcular las operaciones (opción 3).")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

main()