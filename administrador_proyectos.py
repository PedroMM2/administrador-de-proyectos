import json
import time

# Cargar datos desde el archivo JSON
def cargar_datos():
    try:
        with open('administracion.json', 'r') as archivo:  #Abrir el archivo JSON en modo lectura si existe
            return json.load(archivo)  # Carga y devuelve los datos del archivo JSON
    except FileNotFoundError:
        return {}  # Si el archivo no existe, devuelve un diccionario vacío

# Guardar datos en el archivo JSON
def guardar_datos(datos):
    with open('administracion.json', 'w') as archivo:  #Abre el archivo JSON en modo escritura
        json.dump(datos, archivo)  #Guarda los datos en el archivo JSON

administracion = cargar_datos()  #Carga los datos al inicio del programa.
continuar = True
while continuar:
    opcion_entrada = input('1. Agregar nuevas tareas(nombre, descripción y responsable).\
                           \n2. Reasignar responsable.\n3. Actualizar descipción de tarea.\n\
4. Mostrar agenda completa\n5. Salir.\n99. Borrar tarea.\nElige una opción: ')
    if opcion_entrada == '1':
        nombre = input('Introduce el nombre de la tarea: ')
        if nombre in administracion.keys():
            time.sleep(0.5)
            print('----------------------------------------------------------')
            print('Tarea ya agregada, para modificar elige una opción válida:')
            print('----------------------------------------------------------')
            continue
        descripcion = input('Describe esta tarea: ')
        responsable = input('Responsable de la tarea: ')
        administracion[nombre] = {'detalles': descripcion, 'responsable': responsable}  #Agrega la nueva tarea al diccionario
    elif opcion_entrada == '2':
        print('Reasignar responsable.')
        print('----------------------')
        nombre = input('Introduce nombre de la tarea para reasignar responsable: ')
        if nombre in administracion.keys():
            responsable = input(f'Introduce el nuevo responsable para la tarea {nombre}:')
            administracion[nombre]['responsable'] = responsable  # Reasigna el responsable de la tarea existente
        else:
            time.sleep(0.5)
            print('-------------------------------------------------------')
            print('Tarea no agregada, volvemos al menú principal.')
            print('')
    elif opcion_entrada == '3':
        print('Actualizar descripción de una tarea: ')
        print('------------------------------------')
        nombre = input('Introduce nombre de la tarea para actualizar descripción: ')
        if nombre in administracion.keys():
            descripcion = input(f'Nueva descripción de la tarea {nombre}: ')
            administracion[nombre]['detalles'] = descripcion  # Actualiza la descripción de la tarea existente
        else:
            time.sleep(0.5)
            print('-------------------------------------------------------')
            print('Tarea no agregada, volvemos al menú principal.')
            print('')
    elif opcion_entrada =='4':
        time.sleep(0.5)
        print('-------------------------------')
        print('Lista de tareas y responsables:')
        for clave, valor in administracion.items():
            trabajo = valor['detalles']
            respo = valor['responsable']
            print('-------------------------------')
            print(str(clave).title())
            print(str(trabajo).capitalize() + '. ->', 'Responsable:', str(respo).title())
            print('-------------------------------')
    elif opcion_entrada == '99':
        print('Borrar tarea completa.')
        print('----------------------')
        nombre = input('Escribe el nombre de la tarea a borrar:')
        if nombre in administracion.keys():
            del administracion[nombre]  # Borra la tarea del diccionario
        else:
            time.sleep(0.5)
            print('-------------------------------------------------------')
            print('Tarea no encontrada, volviendo al menú principal...')
            print('')
            time.sleep(0.5)
    elif opcion_entrada == '5':
        guardar_datos(administracion)  # Guarda los datos al salir del programa
        print('Saliendo del programa...')
        time.sleep(0.5)
        continuar = False
    else:
        print('Elige una opción válida: ')

guardar_datos(administracion)  # Guarda los datos al salir del programa
