
# 4. Programa "Hola Mundo"

print("hola Mundo")


# 5. Programa que saluda con el nombre ingresado desde teclado

nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}")


# 6. Programa que pide la edad y verifica si es mayor de edad

edad = int(input("Ingrese su edad: "))
if edad >= 18:
 print("Eres mayor de edad.")
else:
 print("Eres menor de edad.")


# 7. Programa que determina si un número es par o impar

numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
  print("El número es par.")
else:
  print("El número es impar.")


# 8. Programa que calcula la suma de 1 hasta el número ingresado

num = int(input("Ingrese un número entero: "))
suma = (num * (num + 1)) // 2  # Fórmula de suma de números enteros
print(f"La suma de los números de 1 hasta {num} es: {suma}")