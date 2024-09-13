# Actividad 1: Registrar Alumno
def registrar_alumno():
    print("Universidad de Python")
    nombre = input("Ingrese su nombre: ")  
    edad = int(input("Ingrese su edad: "))  
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")  

    tiene_titulo_secundario = True  

    monto_matricula = float(input("Ingrese el monto de matrícula: "))  

    cuota = monto_matricula + 1000  

    arancel_python = 3000
    costo_mensual = arancel_python

    descuento = costo_mensual * 0.15
    total = costo_mensual - descuento

    print("\n--- Datos de ingreso ---")  
    print(f"Nombre: {nombre}")  
    print(f"Edad: {edad}")  
    print(f"Fecha de Nacimiento: {fecha_nacimiento}")  
    print(f"Tiene Título Secundario: {tiene_titulo_secundario}")  
    print(f"Monto de Matrícula: ${monto_matricula:.2f}")  
    print(f"Cuota: ${cuota:.2f}")  
    print(f"Arancel mensual de 'Python I': ${costo_mensual:.2f}")  
    print(f"Arancel mensual de 'Python I' con descuento: ${total:.2f}")

# Actividad 2: Evaluar Desempeño
def evaluar_desempeno(nota1, nota2):
    promedio = (nota1 + nota2) / 2

    if nota2 >= 7:
        resultado_examen_final = "Aprobó el examen final"
    else:
        resultado_examen_final = "Desaprobó el examen final"

    if nota2 > nota1:
        desempeño = "Mejoró su desempeño"
    elif nota2 == nota1:
        desempeño = "Mantuvo la nota"
    else:
        desempeño = "Empeoró su desempeño"

    if promedio >= 7:
        resultado_promocion = "Promocionó la materia"
    elif promedio >= 4:
        resultado_promocion = "Debe rendir final"
    else:
        resultado_promocion = "Debe recursar"

    print(f"Promedio: {promedio:.2f}")
    print(resultado_examen_final)
    print(desempeño)
    print(resultado_promocion)

# Actividad 3: Organización de Aulas y Otros
def main():
    dia = int(input("Ingrese el número de día (1 para lunes, 6 para sábado): "))
    if 1 <= dia <= 6:
        aula = "Aula A-300" if dia % 2 == 0 else "Aula A-315"
        print("El aula para el día", dia, "es", aula)
    else:
        print("Número de día inválido. Debe estar entre 1 y 6.")
    
    turno = input("Ingrese el turno (Mañana/Tarde): ").strip().lower()
    num_materias = int(input("Ingrese el número de materias: "))
    cuota = float(input("Ingrese el valor de la cuota: "))
    
    if turno == "tarde" and num_materias > 3:
        descuento = 0.25
    else:
        descuento = 0.05
    
    cuota_descuento = cuota * (1 - descuento)
    print("El valor de la cuota con descuento es: ${:.2f}".format(cuota_descuento))
    
    vehiculo = input("Ingrese el tipo de vehículo (auto/moto/bicicleta): ").strip().lower()
    
    if vehiculo in ["auto", "moto"]:
        costo = 300
    elif vehiculo == "bicicleta":
        costo = 50
    else:
        costo = "Vehículo no válido"
    
    print("El costo de estacionamiento es:", costo)

# Actividad 4: Listado de Aulas
def mostrar_listado_aulas():
    print(f"{'Día':<5} {'Aula':<10}")  
    for dia in range(1, 7): 
        aula = "A-300" if dia % 2 == 0 else "A-315"
        print(f"{dia:<5} {aula:<10}")  

# Actividad 5: Edades y Promedio de Notas
def cargar_edades():
    cargas_erroneas = 0
    edades_validas = []

    while True:
        edad = input("Ingrese una edad (o 'fin' para terminar): ")
        
        if edad.lower() == 'fin':
            break
        
        try:
            edad = int(edad)
            if edad >= 18:
                edades_validas.append(edad)
            else:
                print("Edad inválida, debe ser mayor o igual a 18.")
                cargas_erroneas += 1
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
            cargas_erroneas += 1

    print("Edades ingresadas:", edades_validas)
    print("Cantidad de cargas erróneas:", cargas_erroneas)

def calcular_promedio_notas():
    notas = []

    for i in range(5):
        while True:
            try:
                nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Debe estar entre 0 y 10.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")

    promedio = sum(notas) / len(notas)
    print(f"Promedio de notas: {promedio:.2f}")

def calcular_costo_comedor():
    cuota_por_dia = 1250

    print(f"{'Días':<5} {'Costo Total':<15}")
    for dias in range(1, 7):
        costo_total = cuota_por_dia * dias
        print(f"{dias:<5} ${costo_total:<14}")

# Ejecutar las actividades
if __name__ == "__main__":
    print("Ejecutando Actividad 1: Registrar Alumno")
    registrar_alumno()

    print("\nEjecutando Actividad 2: Evaluar Desempeño")
    nota1 = float(input("Ingrese la nota del primer examen: "))
    nota2 = float(input("Ingrese la nota del segundo examen: "))
    evaluar_desempeno(nota1, nota2)

    print("\nEjecutando Actividad 3: Organización de Aulas y Otros")
    main()

    print("\nEjecutando Actividad 4: Listado de Aulas")
    mostrar_listado_aulas()

    print("\nEjecutando Actividad 5: Edades y Promedio de Notas")
    cargar_edades()
    calcular_promedio_notas()
    calcular_costo_comedor()
