# Encriptador de Archivos

Este es un programa de línea de comandos en Python para encriptar y desencriptar archivos y carpetas. Además de trabajar con líneas de comando, se puede ejecutar en modo interactivo.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
  - [Desde el código fuente](#desde-el-código-fuente)
  - [Usando binarios precompilados](#usando-binarios-precompilados)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
- [Uso](#uso)
  - [Modo Interactivo](#modo-interactivo)
  - [Modo Línea de Comandos](#modo-línea-de-comandos)
- [Compilación de binarios propios](#compilación-de-binarios-propios)
- [Advertencias de Seguridad](#advertencias-de-seguridad)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Características

- Encriptación y desencriptación de archivos individuales
- Encriptación y desencriptación de carpetas completas
- Interfaz de línea de comandos y modo interactivo
- Generación y gestión segura de claves de encriptación

## Requisitos

- Python 3.6+
- Biblioteca cryptography

## Instalación

### Desde el código fuente

1. Clona este repositorio:
   ```bash
   git clone https://github.com/URD0TH/encriptar.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd encriptar
   ```

3. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```

4. Activa el entorno virtual:
   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - En macOS y Linux:
     ```bash
     source venv/bin/activate
     ```

5. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Usando binarios precompilados

Puedes descargar la última versión precompilada para tu sistema operativo desde nuestra página de [Releases](https://github.com/URD0TH/encriptar/releases).

#### Windows
1. Descarga el archivo `encriptador-windows.zip` de la última release.
2. Haz clic derecho en el archivo descargado y selecciona "Extraer todo".
3. Elige una ubicación para extraer los archivos y haz clic en "Extraer".
4. Abre PowerShell o CMD:
   - Para PowerShell: Presiona Win + X y selecciona "Windows PowerShell" o "PowerShell".
   - Para CMD: Presiona Win + R, escribe "cmd" y presiona Enter.
5. Navega hasta la carpeta donde extrajiste los archivos usando el comando `cd`. Por ejemplo:
   ```
   cd C:\Ruta\A\La\Carpeta\Extraida
   ```
6. Ejecuta el programa con:
   ```
   .\encriptador.exe
   ```

#### macOS
1. Descarga el archivo `encriptador-macos.zip` de la última release.
2. Haz doble clic en el archivo descargado para descomprimirlo.
3. Abre una terminal y navega hasta la carpeta donde descomprimiste los archivos:
   ```
   cd /ruta/a/la/carpeta/descomprimida
   ```
4. Haz el archivo ejecutable con el comando:
   ```
   chmod +x encriptador-macos
   ```
5. Ejecuta el programa con:
   ```
   ./encriptador-macos
   ```

#### Linux
1. Descarga el archivo `encriptador-linux.tar.gz` de la última release.
2. Abre una terminal y navega hasta la carpeta donde descargaste el archivo.
3. Descomprime el archivo con:
   ```
   tar -xzvf encriptador-linux.tar.gz
   ```
4. Navega a la carpeta descomprimida:
   ```
   cd encriptador-linux
   ```
5. Haz el archivo ejecutable con el comando:
   ```
   chmod +x encriptador-linux
   ```
6. Ejecuta el programa con:
   ```
   ./encriptador-linux
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
Linux /Mac

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

## Compilación de binarios propios

Si prefieres compilar tus propios binarios, sigue estos pasos:

1. Asegúrate de estar en el directorio del proyecto y tener el entorno virtual activado.

2. Instala PyInstaller:
   ```bash
   pip install pyinstaller
   ```

3. Compila el binario:
   ```bash
   pyinstaller --onefile encriptar.py
   ```

4. El binario compilado se encontrará en la carpeta `dist`.

5. Puedes ejecutar el binario directamente:
   - En Windows:
     ```bash
     .\dist\encriptar.exe
     ```
   - En macOS y Linux:
     ```bash
     ./dist/encriptar
     ```