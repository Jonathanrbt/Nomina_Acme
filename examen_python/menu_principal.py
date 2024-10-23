import time
from modulos_acme.menus import *
from modulos_acme.funciones_acme import *

while True:
    opc = menus_acme('menu principal')
    match opc:
        case '1':
            registro_empleado()
        case '2':
            registro_inasistencias()
        case '3':
            registrar_bonos()
        case '4':
            calcular_nomina()
        case '0':
            print('''
╔═══════════════════════════╗
║  FINALIZANDO PROGRAMA...  ║
╚═══════════════════════════╝''')
            time.sleep(2)
            break
        case _:
            print('''
╔═══════════════════════════════════════════╗
║   PORFAVOR SELECCIONE UNA OPCION VALIDA   ║
║ EL RANGO ESTA ENTRE (1-6). (0) PARA SALIR ║
╚═══════════════════════════════════════════╝''')