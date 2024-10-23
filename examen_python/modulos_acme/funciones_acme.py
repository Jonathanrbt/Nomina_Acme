from modulos_acme.leer_archivos import *
from modulos_acme.menus import *
import datetime
def registro_empleado():
    while True:
        opc = menus_acme('registrar empleado')
        match opc:
            case '1':
                archivo_empleado = leer_archivos('archivo empleados')
                identificacion = input('Ingrese el numero de identificacion: ').strip()
                try:
                    salario = int(input('Ingrese el salario: '))
                except ValueError:
                    print('''
╔═════════════════════════════════════════╗
║¡¡ERROR: DEBE INGRESAR UN NUMERO ENTERO!!║
╚═════════════════════════════════════════╝''')
                    return
                if salario < 1:
                    print('''
╔═══════════════════════════════════════╗
║¡¡EL SALARIO A INGRESAR ES INCORRECTO!!║
╚═══════════════════════════════════════╝''')
                    return
                nombre = input('Ingrese el nombre: ').strip()
                cargo = input('Ingrese el cargo: ').strip()


                if identificacion == '' or nombre == '' or cargo == '':
                    print('''
╔═════════════════════════════════════════════╗
║¡¡ERROR: DEBE INGRESAR AL MENOS UN CARACTER!!║
╚═════════════════════════════════════════════╝''')
                    return
                else:
                    while identificacion in archivo_empleado:
                        identificacion = input('''
╔═════════════════════════════════════════════════════════╗
║  SU IDENTIFICACION YA ES EXISTENTE EN LA BASE DE DATOS  ║
║                 (s). PARA SALIR                         ║
╚═════════════════════════════════════════════════════════╝

Ingrese una nueva identificacion: ''')
                        if identificacion == 's':
                            return
                        if identificacion == '' or nombre == '' or cargo == '':
                            print('''
╔═════════════════════════════════════════════╗
║¡¡ERROR: DEBE INGRESAR AL MENOS UN CARACTER!!║
╚═════════════════════════════════════════════╝''')
                            continue
                

                    archivo_empleado[identificacion]= {
                        'nombre': nombre,
                        'salario': salario,
                        'cargo': cargo,
                        'faltas': 0,
                        'bonos': []
                    }

                    with open('registro_empleados', 'w') as file_empleados:
                        json.dump(archivo_empleado, file_empleados, indent=4)
                    print('\n¡El empleado quedo registrado con exito!')
            case '0':
                print('''
╔════════════════════════════╗
║  SALIENDO DEL REGISTRO...  ║
╚════════════════════════════╝''')
                return
            case _:
                print('''
╔═══════════════════════════════════════════╗
║   PORFAVOR SELECCIONE UNA OPCION VALIDA   ║
║               (0) PARA SALIR              ║
╚═══════════════════════════════════════════╝''')






def registro_inasistencias():
    while True:
        opc = menus_acme('registro inasistencias')
        match opc:
            case '1':
                archivo_empleado = leer_archivos('archivo empleados')
                identificacion = input('\nIngrese el numero de identificacion del empleado: ').strip()
                encontrado = False
                while identificacion in archivo_empleado:
                    encontrado = True
                    try:
                        faltas = int(input(f"\nIngrese el numero de faltas del empleado {archivo_empleado[identificacion]['nombre']}: "))
                    except ValueError:
                        print('''
╔═════════════════════════════════════════╗
║¡¡ERROR: DEBE INGRESAR UN NUMERO ENTERO!!║
╚═════════════════════════════════════════╝''')
                        continue
                    if faltas < 1:
                        print('''
╔════════════════════════════════════════════╗
║¡¡LA INASISTENCIA A INGRESAR ES INCORRECTA!!║
╚════════════════════════════════════════════╝''')
                        continue
                    archivo_empleado[identificacion]['faltas'] += faltas

                    with open('registro_empleados', 'w') as file_empleados:
                        json.dump(archivo_empleado, file_empleados, indent=4)
                    print('\n¡La inasistencia quedo registrada con exito!')
                    return

                if not encontrado:
                    print('''
╔═════════════════════════════════════╗
║  SU EMPLEADO NO HA SIDO ENCONTRADO  ║
╚═════════════════════════════════════╝''')


            case '0':
                print('''
╔═════════════════════════════════════════════╗
║  SALIENDO DEL REGISTRO DE INASISTENCIAS...  ║
╚═════════════════════════════════════════════╝''')
                return
            case _:
                print('''
╔═══════════════════════════════════════════╗
║   PORFAVOR SELECCIONE UNA OPCION VALIDA   ║
║               (0) PARA SALIR              ║
╚═══════════════════════════════════════════╝''')






def registrar_bonos():
    while True:
        opc = menus_acme('registro bonos')
        match opc:
            case '1':
                archivo_empleado = leer_archivos('archivo empleados')
                identificacion = input('\nIngrese el numero de identificacion del empleado: ').strip()
                encontrado = False
                while identificacion in archivo_empleado:
                    encontrado = True
                    try:
                        bono = int(input(f"\nIngrese el monto del bono para el empleado {archivo_empleado[identificacion]['nombre']}: "))
                    except ValueError:
                        print('''
╔═════════════════════════════════════════╗
║¡¡ERROR: DEBE INGRESAR UN NUMERO ENTERO!!║
╚═════════════════════════════════════════╝''')
                        continue
                    concepto = input('\nIngrese el concepto del bono: ')
                    if bono < 1:
                        print('''
╔════════════════════════════════════╗
║¡¡EL BONO A INGRESAR ES INCORRECTO!!║
╚════════════════════════════════════╝''')
                        continue
                    archivo_empleado[identificacion]['bonos'].append(
                        {
                            'valor': bono,
                            'concepto': concepto,
                            'fecha': str(datetime.datetime.today())
                        }
                    )

                    with open('registro_empleados', 'w') as file_empleados:
                        json.dump(archivo_empleado, file_empleados, indent=4)
                    print('\n¡El bono quedo registrado con exito!')
                    return

                if not encontrado:
                    print('''
╔═════════════════════════════════════╗
║  SU EMPLEADO NO HA SIDO ENCONTRADO  ║
╚═════════════════════════════════════╝''')


            case '0':
                print('''
╔═════════════════════════════════════╗
║  SALIENDO DEL REGISTRO DE BONOS...  ║
╚═════════════════════════════════════╝''')
                return
            case _:
                print('''
╔═══════════════════════════════════════════╗
║   PORFAVOR SELECCIONE UNA OPCION VALIDA   ║
║               (0) PARA SALIR              ║
╚═══════════════════════════════════════════╝''')






def calcular_nomina():
    while True:
        opc = menus_acme('calcular nomina')
        match opc:
            case '1':
                archivo_empleado = leer_archivos('archivo empleados')
                encontrado = False
                identificacion = input('\nIngrese el numero de identificacion del empleado: ').strip()
                while identificacion in archivo_empleado:
                    encontrado == True
                    salario_minimo = 1000000
                    total_faltas = archivo_empleado[identificacion]['faltas']
                    salario_base = archivo_empleado[identificacion]['salario']
                    descuento_salud = salario_base * 0.04
                    descuento_pension = salario_base * 0.04
                    auxilio_transporte = 0
                    descontar_novedad = (salario_base / 30) * total_faltas
                    if salario_base < salario_minimo * 2:
                        auxilio_transporte = salario_base * 0.10
                    total_bonos = sum(bono['valor'] for bono in archivo_empleado[identificacion]['bonos'])
                    salario_final= salario_base - (descuento_salud + descuento_pension) - (descontar_novedad) + (total_bonos) + (auxilio_transporte)
                    suma_pagar = (descuento_salud + descuento_pension) + descontar_novedad
                    try:
                        with open(f'{identificacion}.json', 'r') as file_nomina:
                            archivo_nomina = json.load(file_nomina)
                    except (FileNotFoundError, json.JSONDecodeError):
                        archivo_nomina = {}
                    archivo_nomina = {
                        'identificacion': identificacion,
                        'nombre': archivo_empleado[identificacion]['nombre'],
                        'cargo': archivo_empleado[identificacion]['cargo'],
                        'salario': salario_base,
                        'descuento salud': descuento_salud,
                        'descuento pension': descuento_pension,
                        'descuento faltas': descontar_novedad,
                        'bonos': total_bonos,
                        'auxilio transporte': auxilio_transporte,
                        'total a pagar': suma_pagar,
                        'salario final': salario_final,
                        'fecha nomina': str(datetime.datetime.today())
                    }
                    
                    
                    with open(f'{identificacion}.json', 'w') as file_nomina:
                        json.dump(archivo_nomina, file_nomina, indent=4)
                        
                    return
                if not encontrado:
                    print('''
╔═════════════════════════════════════╗
║  SU EMPLEADO NO HA SIDO ENCONTRADO  ║
╚═════════════════════════════════════╝''')


            case '0':
                print('''
╔═════════════════════════════════════╗
║  SALIENDO DEL REGISTRO DE BONOS...  ║
╚═════════════════════════════════════╝''')
                return
            case _:
                print('''
╔═══════════════════════════════════════════╗
║   PORFAVOR SELECCIONE UNA OPCION VALIDA   ║
║               (0) PARA SALIR              ║
╚═══════════════════════════════════════════╝''')