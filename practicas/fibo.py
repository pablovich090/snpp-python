

# Función para generar la secuencia de Fibonacci hasta un cierto límite
def fibonacci_hasta_100():
    # Inicializamos los dos primeros números de la secuencia
    a, b = 0, 1
    
    # Iteramos mientras el siguiente número en la secuencia sea menor o igual que 100
    while a <= 100:
        print(a, end=" ")  # Imprimir el número actual de la secuencia
        a, b = b, a + b   # Calcular los siguientes números de la secuencia

# Llamar a la función para imprimir solo los números de la serie de Fibonacci hasta 100
fibonacci_hasta_100()
