def menus_acme(operacion):
    if operacion == 'menu principal':
        opcion = input('''
╔═════════════════════╗
║  GESTION DE NOMINA  ║
╚═════════════════════╝

(1). Registro de empleados.
(2). Registro de inasistencia.
(3). Registro de bonos extra-legales.
(4). Cálculo de la nómina.
(0). Salir de programa.

Seleccione algunas de las opciones: ''')
        return opcion
    if operacion == 'registrar empleado':
        opc = input('''
╔══════════════════════╗
║  REGISTRAR EMPLEADO  ║
╚══════════════════════╝

(1). Continuar con el registro.
(0). Salir del registro.

Seleccione alguna de las opciones: ''')
        return opc
    if operacion == 'registro inasistencias':
        opc = input('''
╔════════════════════════════════════════╗
║  REGISTRAR INASISTENCIAS DEL EMPLEADO  ║
╚════════════════════════════════════════╝

(1). Continuar con el registro.
(0). Salir del registro.

Seleccione alguna de las opciones: ''')
        return opc
    if operacion == 'registro bonos':
        opc = input('''
╔════════════════════════════════╗
║  REGISTRAR BONOS DEL EMPLEADO  ║
╚════════════════════════════════╝

(1). Continuar con el registro.
(0). Salir del registro.

Seleccione alguna de las opciones: ''')
        return opc
    if operacion == 'calcular nomina':
        opc = input('''
╔════════════════════════════════╗
║  CALCULAR NOMINA DEL EMPLEADO  ║
╚════════════════════════════════╝

(1). Continuar con el calculo.
(0). Salir del calculo.

Seleccione alguna de las opciones: ''')
        return opc