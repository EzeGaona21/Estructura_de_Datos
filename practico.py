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





#PRACTICO NUMERO 2





def mayor_unico(num1, num2, num3):
    # Encuentra el mayor único entre tres números positivos
    if (num1 > num2 and num1 > num3):
        if (num2 < num1 and num3 < num1):
            return num1
    elif (num2 > num1 and num2 > num3):
        if (num1 < num2 and num3 < num2):
            return num2
    elif (num3 > num1 and num3 > num2):
        if (num1 < num3 and num2 < num3):
            return num3
    return "No existe un mayor único"

def main_actividad1():
    num1 = int(input("Ingrese el primer número positivo: "))
    num2 = int(input("Ingrese el segundo número positivo: "))
    num3 = int(input("Ingrese el tercer número positivo: "))
    
    resultado = mayor_unico(num1, num2, num3)
    print("El mayor único es:", resultado)

def es_fecha_valida(dia, mes, anio):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False
    return True

def main_actividad2():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    
    if es_fecha_valida(dia, mes, anio):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")

def desglosar_cambio(compra, monto_entregado):
    cambio = monto_entregado - compra
    if cambio < 0:
        return "Monto entregado es insuficiente"
    
    billetes = [500, 100, 50, 20, 10, 5]
    resultado = {}
    
    for billete in billetes:
        if cambio >= billete:
            cantidad = cambio // billete
            resultado[billete] = cantidad
            cambio %= billete
    
    return resultado

def main_actividad3():
    compra = float(input("Ingrese el valor de la compra: "))
    monto_entregado = float(input("Ingrese el monto entregado: "))
    
    cambio = desglosar_cambio(compra, monto_entregado)
    
    if isinstance(cambio, str):
        print(cambio)
    else:
        print("Desglose del cambio:")
        for billete, cantidad in cambio.items():
            print(f"${billete}: {cantidad}")

def calcular_precio_total(cantidad, descuento):
    precio_unitario = 10
    total = cantidad * precio_unitario
    total_descuento = total * (1 - descuento / 100)
    return total_descuento

def emitir_recibo(cantidad):
    descuentos = [5, 15, 20]
    print("Nombre de la empresa: Zapallos SA")
    print("Tipo de moneda: Pesos")
    for descuento in descuentos:
        total_a_pagar = calcular_precio_total(cantidad, descuento)
        print(f"Total a pagar con {descuento}% de descuento: ${total_a_pagar:.2f}")

def main_actividad4():
    cantidad = int(input("Ingrese la cantidad de zapallos: "))
    emitir_recibo(cantidad)

def main():
    print("Ejecutando Actividad 1: Mayor Único")
    main_actividad1()
    
    print("\nEjecutando Actividad 2: Verificar Fecha Válida")
    main_actividad2()
    
    print("\nEjecutando Actividad 3: Desglosar Cambio")
    main_actividad3()
    
    print("\nEjecutando Actividad 4: Precio con Descuentos")
    main_actividad4()

if __name__ == "__main__":
    main()
