import math

def sumar(a: float, b: float) -> float:
    """Calcula la suma de dos números flotantes
    
    Args:
        a: Primer número.
        b: Segundo número.
    
    Returns:
        float: Resultado de la suma.
    """
    return a + b

def restar(a: float, b: float) -> float:
    """Calcula la resta de dos números flotantes
    
    Args:
        a: Primer número.
        b: Segundo número.
    
    Returns:
        float: Resultado de la resta.
    """
    return a - b

def dividir(a: float, b: float) -> float:
    """Calcula la división de dos números flotantes
    
    Args:
        a: Primer número.
        b: Segundo número.
    
    Returns:
        float: Resultado de la división, o un mensaje de error si b es cero.
    """
    if b == 0:
        return "No es posible dividir por cero"
    return a / b

def multiplicar(a: float, b: float) -> float:
    """Calcula la multiplicación de dos números flotantes
    
    Args:
        a: Primer número.
        b: Segundo número.
    
    Returns:
        float: Resultado de la multiplicación.
    """
    return a * b

def calcular_factorial(n: int) -> int:
    """Calcula el factorial de un número.
    
    Args:
        n: Número entero.
    
    Returns:
        int: Factorial del número.
    """
    if n < 0:
        return "Factorial no definido para números negativos"
    return math.factorial(n)