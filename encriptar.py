from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken
import base64
import os
import getpass
from cryptography.hazmat.primitives import hashes
import argparse
import sys

def cargar_clave_con_password(password):
    if not isinstance(password, bytes):
        password = password.encode()
    
    with open("salt.salt", "rb") as salt_archivo:
        salt = salt_archivo.read()
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    clave = base64.urlsafe_b64encode(kdf.derive(password))
    return clave

def generar_clave_con_password(password):
    # Verificamos si password ya es bytes, si no, lo convertimos
    if not isinstance(password, bytes):
        password = password.encode()
    
    salt = os.urandom(16)
    
    with open("salt.salt", "wb") as salt_archivo:
        salt_archivo.write(salt)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    clave = base64.urlsafe_b64encode(kdf.derive(password))
    
    with open("clave.key", "wb") as clave_archivo:
        clave_archivo.write(clave)
    
    return clave

def encriptar_archivo(ruta, clave, patrones_exclusion=None):
    if not isinstance(clave, bytes):
        raise ValueError("Se esperaba una clave en bytes, no una contraseña")
    
    # Verificar si el archivo debe ser excluido
    if patrones_exclusion and not debe_procesar_archivo(ruta, patrones_exclusion):
        print(f"Excluido: {ruta}")
        return False
    
    fernet = Fernet(clave)
    
    try:
        with open(ruta, 'rb') as archivo:
            archivo_datos = archivo.read()
        
        archivo_encriptado = fernet.encrypt(archivo_datos)
        
        with open(ruta, 'wb') as archivo:
            archivo.write(archivo_encriptado)
        
        print(f"El archivo {ruta} ha sido encriptado exitosamente.")
        return True
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {ruta}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {str(e)}")
    return False

def desencriptar_archivo(ruta, clave, patrones_exclusion=None):
    # Verificar si el archivo debe ser excluido
    if patrones_exclusion and not debe_procesar_archivo(ruta, patrones_exclusion):
        print(f"Excluido: {ruta}")
        return False
        
    fernet = Fernet(clave)
    try:
        with open(ruta, 'rb') as archivo:
            datos_encriptados = archivo.read()
        try:
            datos_desencriptados = fernet.decrypt(datos_encriptados)
            with open(ruta, 'wb') as archivo:
                archivo.write(datos_desencriptados)
            print(f"El archivo {ruta} ha sido desencriptado exitosamente.")
            return True
        except InvalidToken:
            print("Error: La clave proporcionada no es válida para este archivo.")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {ruta}")
    except Exception as e:
        print(f"Error al desencriptar el archivo: {str(e)}")
    return False

def encriptar_carpeta(carpeta_ruta, password, patrones_exclusion=None):
    if patrones_exclusion and isinstance(patrones_exclusion, str):
        patrones_exclusion = [p.strip() for p in patrones_exclusion.split(',')]
    
    archivos_procesados = 0
    archivos_excluidos = 0
    
    for root, dirs, files in os.walk(carpeta_ruta):
        for nombre_archivo in files:
            archivo_ruta = os.path.join(root, nombre_archivo)
            if debe_procesar_archivo(archivo_ruta, patrones_exclusion):
                encriptar_archivo(archivo_ruta, password)
                archivos_procesados += 1
            else:
                print(f"Excluido: {archivo_ruta}")
                archivos_excluidos += 1
    
    print(f"Carpeta {carpeta_ruta} procesada:")
    print(f"- Archivos encriptados: {archivos_procesados}")
    print(f"- Archivos excluidos: {archivos_excluidos}")

def desencriptar_carpeta(carpeta_ruta, password, patrones_exclusion=None):
    if patrones_exclusion and isinstance(patrones_exclusion, str):
        patrones_exclusion = [p.strip() for p in patrones_exclusion.split(',')]
    
    archivos_procesados = 0
    archivos_excluidos = 0
    
    for root, dirs, files in os.walk(carpeta_ruta):
        for nombre_archivo in files:
            archivo_ruta = os.path.join(root, nombre_archivo)
            if debe_procesar_archivo(archivo_ruta, patrones_exclusion):
                desencriptar_archivo(archivo_ruta, password)
                archivos_procesados += 1
            else:
                print(f"Excluido: {archivo_ruta}")
                archivos_excluidos += 1
    
    print(f"Carpeta {carpeta_ruta} procesada:")
    print(f"- Archivos desencriptados: {archivos_procesados}")
    print(f"- Archivos excluidos: {archivos_excluidos}")

def verificar_clave_existente():
    ruta_clave = "clave.key"
    if os.path.exists(ruta_clave):
        while True:
            respuesta = input("Ya existe una clave. ¿Desea mantenerla? (s/n): Defecto (s): ").lower() or 's'
            if respuesta == 's':
                print("Se usará la clave existente.")
                return True
            elif respuesta == 'n':
                print("ADVERTENCIA: Si genera una nueva clave, no será posible recuperar los archivos encriptados anteriormente.")
                confirmacion = input("¿Está seguro de que desea generar una nueva clave? (s/n): Defecto (n): ").lower() or 'n'
                if confirmacion == 's':
                    return False
                elif confirmacion == 'n':
                    print("Se usará la clave existente.")
                    return True
            print("Por favor, responda 's' para sí o 'n' para no.")
    else:
        print("No se encontró una clave existente. Se generará una nueva.")
        return False

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Encripta o desencripta archivos y carpetas.",
        epilog="Ejemplos de uso:\n"
               "  python encriptar.py -ea -r ./archivo.txt\n"
               "  python encriptar.py -ec -r ./carpeta -p micontraseña -e *.txt,*.log\n"
               "  python encriptar.py -da -r ./archivo_encriptado.txt\n"
               "  python encriptar.py -dc -r ./carpeta_encriptada\n"
               "ADVERTENCIA: Proporcionar la contraseña como argumento de línea de comandos puede ser un riesgo de seguridad.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-ea", "--encriptar-archivo", action="store_true", help="Encriptar un archivo")
    group.add_argument("-ec", "--encriptar-carpeta", action="store_true", help="Encriptar una carpeta")
    group.add_argument("-da", "--desencriptar-archivo", action="store_true", help="Desencriptar un archivo")
    group.add_argument("-dc", "--desencriptar-carpeta", action="store_true", help="Desencriptar una carpeta")
    parser.add_argument("-r", "--ruta", help="Ruta del archivo o carpeta a procesar")
    parser.add_argument("-p", "--password", help="Contraseña para la clave (ADVERTENCIA: usar este argumento puede ser un riesgo de seguridad)")
    parser.add_argument("-e", "--excluir", help="Patrones de archivos o carpetas a excluir (separados por comas). Ejemplo: *.txt,*.log,carpeta1")
    return parser.parse_args()

def menu_interactivo():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Encriptar archivo")
        print("2. Encriptar carpeta")
        print("3. Desencriptar archivo")
        print("4. Desencriptar carpeta")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '5':
            print("Gracias por usar el programa. ¡Hasta luego!")
            sys.exit(0)
        
        if opcion in ['1', '2', '3', '4']:
            ruta = input("Ingrese la ruta del archivo o carpeta: ")
            exclusiones = input("Ingrese patrones de exclusión (separados por comas) o presione Enter para no excluir nada: ")
            return opcion, ruta, exclusiones
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def debe_procesar_archivo(archivo_ruta, patrones_exclusion):
    if not patrones_exclusion:
        return True
    
    from fnmatch import fnmatch
    nombre_archivo = os.path.basename(archivo_ruta)
    
    for patron in patrones_exclusion:
        if fnmatch(nombre_archivo, patron.strip()) or fnmatch(archivo_ruta, patron.strip()):
            return False
    return True

def main():
    args = parse_arguments()
    
    if len(sys.argv) > 1:
        # Modo línea de comandos
        ruta = args.ruta
        exclusiones = args.excluir
        if args.encriptar_archivo:
            opcion = '1'
        elif args.encriptar_carpeta:
            opcion = '2'
        elif args.desencriptar_archivo:
            opcion = '3'
        elif args.desencriptar_carpeta:
            opcion = '4'
        else:
            print("Debe especificar una acción (-ea, -ec, -da, -dc)")
            sys.exit(1)
        
        if not ruta:
            print("Debe especificar una ruta con el argumento -r")
            sys.exit(1)
    else:
        # Modo interactivo
        opcion, ruta, exclusiones = menu_interactivo()
    
    clave_existente = verificar_clave_existente()
    if args.password:
        password = args.password
        print("ADVERTENCIA: Usar la contraseña como argumento de línea de comandos puede ser un riesgo de seguridad.")
    elif clave_existente:
        password = getpass.getpass("Ingrese la contraseña para la clave existente: ")
    else:
        password = getpass.getpass("Ingrese una nueva contraseña para generar la clave: ")

    if clave_existente:
        clave = cargar_clave_con_password(password)
    else:
        clave = generar_clave_con_password(password)

    if clave is None:
        print("Error: No se pudo generar o cargar la clave.")
        return

    print(f"Clave cargada/generada: {clave[:10]}...") # Imprime los primeros 10 caracteres de la clave

    if opcion == '1':
        encriptar_archivo(ruta, clave, exclusiones)
    elif opcion == '2':
        encriptar_carpeta(ruta, clave, exclusiones)
    elif opcion == '3':
        desencriptar_archivo(ruta, clave, exclusiones)
    elif opcion == '4':
        desencriptar_carpeta(ruta, clave, exclusiones)

    if len(sys.argv) == 1:
        input("Presione Enter para volver al menú principal...")
        main()  # Vuelve al menú principal en modo interactivo

if __name__ == "__main__":
    main()