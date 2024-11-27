import math
#Ejercicios: Nivel 2
#Comprueba el tipo de datos de todas tus variables usando la función incorporada type()
name = "Rodrigo Alberto"
print(type(name))

#Usando la función incorporada len() , encuentre la longitud de su nombre
print(f"La longitud del nombre es {len(name)} caracteres")

#Compara la longitud de tu nombre y tu apellido
last_name = 'Carrasco'

print(f"La longitud de mi nombre es {len(name)} y la de mi apellido es {len(last_name)} siendo el mayo {name if name > last_name else last_name}")

#Declara 5 como num_one y 4 como num_two
num_one = 5
num_two = 4

#Sume num_one y num_two y asigne el valor a una variable total
total = num_one + num_two

#Resta num_two de num_one y asigna el valor a una variable diff
diff = num_two - num_one

#Multiplica num_two y num_one y asigna el valor a una variable producto
producto = num_two * num_one

#Dividir num_one por num_two y asignar el valor a una variable división
division = num_one / num_two

#Utilice la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable
resto = num_two % num_one

#Calcula num_one a la potencia de num_two y asigna el valor a una variable exp
exp = num_one ** num_two

#Encuentra la división del piso de num_one por num_two y asigna el valor a una variable floor_division
floor_division = num_one // num_two

#El radio de un círculo es de 30 metros.
#Calcula el área de un círculo y asigna el valor a una variable llamada area_of_circle
radio = 30
area_of_circle = math.pi * (radio**2)

#Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circum_of_circle
circum_of_circle = 2 * math.pi * radio

#Tome el radio como entrada del usuario y calcule el área.
radio_usuario = int(input("Ingrese el radio: "))
area_of_circle_user = math.pi * (radio_usuario**2)

#Utilice la función de entrada incorporada para obtener el nombre, apellido, país y edad 
# de un usuario y almacenar el valor en sus nombres de variable correspondientes.
name_two = input("Ingresa tu nombre: ")
last_name_two = input("Ingresa tu apellido: ")
country_two = input("Ingresa tu pais: ")
age_two = int(input("Ingresa tu edad: "))

#Ejecute help('keywords') en el shell de Python o en su archivo para verificar las palabras o palabras clave reservadas de Python