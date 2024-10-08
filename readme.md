# Encriptador de Archivos

Este es un programa de línea de comandos en Python para encriptar y desencriptar archivos y carpetas. Además de trabajar con lineas de comando, se puede ejecutar en modo interactivo.

## Características

- Encriptación y desencriptación de archivos individuales
- Encriptación y desencriptación de carpetas completas
- Interfaz de línea de comandos y modo interactivo
- Generación y gestión segura de claves de encriptación

## Requisitos

- Python 3.6+
- Biblioteca cryptography

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/encriptador-archivos.git
   ```

2. Crea un entorno virtual:
   ```
   python -m venv venv
   ```

3. Activa el entorno virtual:
   - En Windows:
     ```
     .\venv\Scripts\activate
     ```
   - En macOS y Linux:
     ```
     source venv/bin/activate
     ```

4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

### Modo Interactivo

Ejecuta el script sin argumentos para entrar en el modo interactivo:

```
python encriptar.py
```

Sigue las instrucciones en pantalla para seleccionar la operación y proporcionar la ruta del archivo o carpeta.

### Modo Línea de Comandos

Usa los siguientes argumentos para ejecutar operaciones específicas:

- `-h` o `--help`: Mostrar ayuda
- `-ea` o `--encriptar-archivo`: Encriptar un archivo
- `-ec` o `--encriptar-carpeta`: Encriptar una carpeta
- `-da` o `--desencriptar-archivo`: Desencriptar un archivo
- `-dc` o `--desencriptar-carpeta`: Desencriptar una carpeta
- `-r` o `--ruta`: Ruta del archivo o carpeta a procesar
- `-p` o `--password`: Contraseña para la clave (opcional, no recomendado por seguridad)

Ejemplos:
Python
```
python encriptar.py -ea -r ./archivo.txt
python encriptar.py -ec -r ./carpeta
python encriptar.py -da -r ./archivo_encriptado.txt
python encriptar.py -dc -r ./carpeta_encriptada
```
Windows

```
python encriptar.exe -ea -r .\archivo.txt
python encriptar.exe -ec -r .\carpeta
python encriptar.exe -da -r .\archivo_encriptado.txt
python encriptar.exe -dc -r .\carpeta_encriptada
```
Linux

```
python encriptar.bin -ea -r /ruta/archivo.txt
python encriptar.bin -ec -r /ruta/carpeta
python encriptar.bin -da -r /ruta/archivo_encriptado.txt
python encriptar.bin -dc -r /ruta/carpeta_encriptada
```

## Creación de Binarios

Para crear un ejecutable del programa, puedes usar PyInstaller:

1. Crea un entorno virtual:
   ```
   python -m venv venv
   ```

2. Activa el entorno virtual:
   - En Windows:
     ```
     .\venv\Scripts\activate
     ```
   - En macOS y Linux:
     ```
     source venv/bin/activate
     ```

3. Instala PyInstaller en el entorno virtual:
   ```
   pip install pyinstaller
   ```

4. Crea el ejecutable:
   ```
   pyinstaller --onefile encriptar.py
   ```

5. El ejecutable se creará en la carpeta `dist`.

## Advertencias de Seguridad

- No comparta su clave de encriptación o contraseña.
- Evite usar la opción `-p` en la línea de comandos, ya que la contraseña podría quedar registrada en el historial.
- Guarde una copia de seguridad de sus archivos originales antes de encriptarlos.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.