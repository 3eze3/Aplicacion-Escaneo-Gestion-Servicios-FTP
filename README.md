# Aplicación de Escaneo y Gestión de Servicios FTP

## Descripción

Esta es una aplicación gráfica desarrollada en Python utilizando `tkinter` para escanear y gestionar servicios FTP en una red. La aplicación permite a los usuarios:

-   Escanear una red para identificar servidores FTP.
-   Intentar autenticarse con credenciales anónimas o forzar contraseñas conocidas utilizando Hydra.
-   Guardar los resultados en un archivo y permitir la edición de los mismos.

## Requisitos

-   Python 3.x
-   Tkinter
-   Hydra
-   Archivo de contraseñas `rockyou.txt`

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/3eze3/Aplicacion-Escaneo-Gestion-Servicios-FTP
    cd Enumeracion_servicios_tkinter
    ```

2. Instala los requisitos necesarios:
    - **Tkinter**: Debería estar incluido en la mayoría de las instalaciones de Python.
    - **Hydra**:
        ```bash
        sudo apt-get install hydra
        ```
    - **rockyou.txt**:
        - Descarga el archivo `rockyou.txt` desde [SecLists](https://github.com/danielmiessler/SecLists) y colócalo en la ruta `/usr/share/wordlists/`.

## Uso

1. Ejecuta la aplicación:

    ```bash
    python3 escaneo_gestion_servicios_FTP.py
    ```

2. Interfaz gráfica:
    - **Escaneo FTP**: Ingresa la IP y el usuario (opcional) y presiona el botón "Escanear FTP".
    - **Forzar contraseñas**: Ingresa la IP y el usuario, luego presiona el botón "Forzar contraseñas". Asegúrate de tener `rockyou.txt` en la ruta especificada.
    - **Menú Archivo**: Permite crear un nuevo archivo, abrir un archivo existente, guardar los resultados actuales o guardarlos como un nuevo archivo.
    - **Menú Ayuda**: Proporciona información sobre la aplicación.

## Funcionalidades

-   **Escaneo de Red**: Detecta servidores FTP en la red.
-   **Autenticación Anónima**: Intenta autenticarse en servidores FTP utilizando credenciales anónimas.
-   **Fuerza Bruta de Contraseñas**: Utiliza Hydra para intentar forzar contraseñas utilizando un archivo de diccionario (`rockyou.txt`).
-   **Gestión de Archivos**: Permite abrir, editar y guardar resultados de escaneo.

## Contribuciones

Las contribuciones son bienvenidas. Para reportar errores o sugerir mejoras, abre un issue o envía un pull request en GitHub.

## Agradecimientos

-   Gracias a [SecLists](https://github.com/danielmiessler/SecLists) por proporcionar el archivo `rockyou.txt`.
-   Gracias a Gareth Flowers por el [FTP Server Docker Image](https://github.com/garethflowers/docker-ftp-server) utilizado para probar esta aplicación.

### Cómo usar la imagen de FTP Server

Para iniciar una instancia del servidor FTP, con los datos almacenados en `/data` en el host, usa lo siguiente:

```bash
docker run \
    --detach \
    --env FTP_PASS=123 \
    --env FTP_USER=user \
    --name my-ftp-server \
    --publish 20-21:20-21/tcp \
    --publish 40000-40009:40000-40009/tcp \
    --volume /data:/home/user \
    garethflowers/ftp-server
```
