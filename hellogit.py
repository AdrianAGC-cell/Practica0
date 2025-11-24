# Importamos el módulo 'datetime' para obtener el año actual
import datetime

# --- Pide el nombre y el año de nacimiento al usuario ---
nombre = input("Hola! ¿Cuál es tu nombre? ")
print(f"¡Bienvenido, {nombre}!")

# Pedimos el año y nos aseguramos de que sea un número entero
while True:
    try:
        año_nacimiento = int(input("¿En qué año naciste (ej: 1990)? "))
        break
    except ValueError:
        print("Por favor, introduce solo números para el año.")

# --- Realiza el cálculo de la edad ---
año_actual = datetime.date.today().year

# Calculamos la edad de forma aproximada
edad_aproximada = año_actual - año_nacimiento

# --- Muestra el resultado ---
print("-" * 30)
print(f"¡{nombre}, tu edad aproximada es de {edad_aproximada} años!")
print("-" * 30)