"""La compañía Rappi, solicita un sistema que determine los días de vacaciones a los que tiene derecho un trabajador, tomando en cuenta las siguientes características:

Existen tres departamentos dentro de la compañía con sus respectivas claves:

1.Departamento de atención al cliente. (Clave 1)
2.Departamento de Logística. (Clave 2)
3. Gerencia. (Clave 3)

Trabajadores con clave 1 (Atención al cliente):
*Con 1 año de servicio, reciben 6 días de vacaciones.
*Con 2 a 6 años de servicio, reciben 14 días de vacaciones.
*A partir de 7 años de servicio, reciben 20 días de vacaciones.

Trabajadores con clave 2 (Logística):
*Con 1 año de servicio, reciben 7 días de vacaciones.
*Con 2 a 6 años de servicio, reciben 15 días de vacaciones.
*A partir de 7 años de servicio, reciben 22 días de vacaciones.

Trabajadores con clave 3 (Gerencia):
*Con 1 año de servicio, reciben 10 días de vacaciones.
*Con 2 a 6 años de servicio, reciben 20 días de vacaciones.
*A partir de 7 años de servicio, reciben 30 días de vacaciones.


Requerimientos indispensables:

El sistema debe solicitar el "Nombre", "Clave de departamento" y "antigüedad" del trabajador.
Posteriormente el programa debe mostrar un mensaje en pantalla que contenga el nombre del trabajador y los días de vacaciones a los que tiene derecho"""


nombre = input("!Hola, ingresa tu nombre y oprime enter: ")
departamento = int(input("""
Ingresa el numero de tu departamento y oprime enter:
1-Departamento de atención al cliente.
2-Departamento de Logística.
3-Gerencia.
: """))
antiguedad = int(input("Ingresa tus años de antigüedad y oprime enter : "))

if departamento == 1:
    if antiguedad == 1:
        print(f"{nombre} perteneces al departamento de Atención al cliente, tienes {antiguedad} años de antigüedad y te corresponden 6 días de vacaciones.")
    elif antiguedad > 1 and antiguedad < 7:
        print(f"{nombre} perteneces al departamento de Atención al cliente, tienes {antiguedad} años de antigüedad y te corresponden 14 días de vacaciones.")
    elif antiguedad > 7:
        print(f"{nombre} perteneces al departamento de Atención al cliente, tienes {antiguedad} años de antigüedad y te corresponden 20 días de vacaciones.")
elif departamento == 2:
    if antiguedad == 1:
        print(f"{nombre} perteneces al departamento de Logística, tienes {antiguedad} años de antigüedad y te corresponden 7 días de vacaciones.")
    elif antiguedad > 1 and antiguedad < 7:
        print(f"{nombre} perteneces al departamento de Logística, tienes {antiguedad} años de antigüedad y te corresponden 15 días de vacaciones.")
    elif antiguedad > 7:
        print(f"{nombre} perteneces al departamento de Logística, tienes {antiguedad} años de antigüedad y te corresponden 22 días de vacaciones.")
elif departamento == 3:
    if antiguedad == 1:
        print(f"{nombre} perteneces al departamento de Gerencia, tienes {antiguedad} años de antigüedad y te corresponden 10 días de vacaciones.")
    elif antiguedad > 1 and antiguedad < 7:
        print(f"{nombre} perteneces al departamento de Gerencia, tienes {antiguedad} años de antigüedad y te corresponden 20 días de vacaciones.")
    elif antiguedad > 7:
        print(f"{nombre} perteneces al departamento de Gerencia, tienes {antiguedad} años de antigüedad y te corresponden 30 días de vacaciones.")
else:
    print("El numero ingresado no corresponde a un departamento de la empresa.")
