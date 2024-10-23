import json
def leer_archivos(opc):
    if opc == 'archivo empleados':
        try:
            with open('registro_empleados', 'r') as file_empleados:
                return json.load(file_empleados)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}