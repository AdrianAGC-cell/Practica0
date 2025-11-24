
import datetime

nombre = input("Hola! ¿Cuál es tu nombre? ")
print(f"¡Bienvenido, {nombre}!")

while True:
    try:
        año_nacimiento = int(input("¿En qué año naciste (ej: 1990)? "))
        break
    except ValueError:
        print("Por favor, introduce solo números para el año.")

año_actual = datetime.date.today().year
]
edad_aproximada = año_actual - año_nacimiento

print("-" * 30)
print(f"¡{nombre}, tu edad aproximada es de {edad_aproximada} años!")
print("-" * 30)