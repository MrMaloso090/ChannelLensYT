====================================================================================================================================================================== ENGLISH
====================================================================================================================================================================== ENGLISH 


# ChannelLensYT - YouTube Channel Analyzer and Power BI Auto-Updater

This project is designed to analyze YouTube channels, retrieve their data through the YouTube API, and then automatically update a Power BI presentation with the latest data.

## Description

**ChannelLensYT** is a tool that uses the YouTube API to download data from YouTube channels and videos. The program allows:

- Downloading detailed information about all videos from a YouTube channel.
- Processing and storing data in an SQLite database.
- Generating and updating Power BI presentations with the obtained data.
- Extracting and analyzing video comments for a deeper engagement study.

## Features

- **YouTube V3 API**: Uses the YouTube API to retrieve information about channels, videos, and comments.
- **Comment Downloading**: Extracts up to 100 comments per video, including author details and engagement metrics.
- **Power BI Update**: After downloading the data, the program automatically updates a Power BI presentation.
- **Command-line Interface**: Users can choose to change the API key, analyze a YouTube channel, or get instructions on obtaining an API key.

## Instructions for Executable (.exe) Users

If you just want to use the program without interacting with the source code, follow these steps:

1. **Install Power BI Desktop and the SQLite ODBC Connector**.
   - Download Power BI Desktop here: [https://powerbi.microsoft.com/desktop/](https://powerbi.microsoft.com/desktop/)
   - Download the SQLite ODBC Connector here (latest version): [http://www.ch-werner.de/sqliteodbc/](http://www.ch-werner.de/sqliteodbc/)

2. **Obtain a YouTube V3 API Key** if you plan to use it frequently. Instructions are available in menu option 3.

3. **Run the .exe file** (double-click on the executable file).

4. **Enter the YouTube channel URL** when prompted.

5. **Wait** for the program to download the data and automatically update the Power BI presentation.

## Instructions for Programmers and Developers

### Requirements

1. **Power BI Desktop**: Must be installed to update presentations.
   - Download here: [https://powerbi.microsoft.com/desktop/](https://powerbi.microsoft.com/desktop/)

2. **SQLite ODBC Connector**: Required for Power BI to connect to the SQLite database.
   - Download here (latest version): [http://www.ch-werner.de/sqliteodbc/](http://www.ch-werner.de/sqliteodbc/)

3. **Python 3.x**: Required to run scripts for analysis, data retrieval, and presentation updates.
   - Download here: [https://www.python.org/](https://www.python.org/)

4. **Required Python Libraries**:
   - `pyautogui`: Simulates the F5 key to refresh the presentation.
   - `googleapiclient.discovery`: Interacts with the YouTube API.
   - `dotenv`: Loads API keys from a `.env` file.
   - `requests`: Performs HTTP requests.
   - `sqlite3`: Manages the database.
   - `re`, `os`, `shutil`, `time`, `sys`: Handles file manipulation and flow control.

   Install all required libraries with the following command:
   ```bash
   pip install -r requirements.txt
   ```

5. **YouTube API Key**:
   - If you plan to use the program frequently, you need a free YouTube V3 API key.
   - You can obtain it by following the instructions in **menu option 3** of the program.
   - If you are only running a few tests, changing the API key is unnecessary.

### Installation

1. **Install Python 3.x**
2. **Install the required libraries**
3. **Install Power BI and the SQLite connector**
4. **Obtain a YouTube API key** if necessary.

### Instructions

1. **Run the program manually**:
   ```bash
   python main.py
   ```

2. **Interaction**:
   When you run the program, you will see a menu with three options:

   - **Option 1**: Change the YouTube API key (only necessary for frequent use).
   - **Option 2**: Analyze a YouTube channel and retrieve video comments.
   - **Option 3**: Instructions for obtaining an API key.

3. **Process**:
   - Selecting **Option 2** will prompt the program to download information from the entered YouTube channel, including video comments, save it to the database, and then launch the interactive Power BI presentation.

## License

This project is licensed under the MIT License.


====================================================================================================================================================================== ESPAÑOL
====================================================================================================================================================================== ESPAÑOL


# ChannelLensYT - YouTube Channel Analyzer and Power BI Auto-Updater

Este proyecto está diseñado para analizar canales de YouTube, recuperar sus datos a través de la API de YouTube y luego actualizar automáticamente una presentación de Power BI con los datos más recientes.

## Descripción

**ChannelLensYT** es una herramienta que utiliza la API de YouTube para descargar datos de canales y videos de YouTube. El programa permite:

- Descargar información detallada sobre todos los videos de un canal de YouTube.
- Procesar y almacenar los datos en una base de datos SQLite.
- Generar y actualizar presentaciones en Power BI con los datos obtenidos.
- Extraer y analizar comentarios de videos para un estudio más profundo del engagement.

## Características

- **API YouTube V3**: Utiliza la API de YouTube para recuperar información sobre canales, videos y comentarios.
- **Descarga de comentarios**: Permite extraer hasta 100 comentarios por video, incluyendo datos del autor y engagement.
- **Actualización de Power BI**: Después de descargar los datos, el programa actualiza una presentación de Power BI automáticamente.
- **Interfaz de línea de comandos**: El usuario puede elegir entre cambiar la clave de la API, analizar un canal de YouTube o obtener instrucciones sobre cómo obtener una clave de API.

## Instrucciones para usuarios del ejecutable (.exe)

Si solo deseas usar el programa sin interactuar con el código fuente, sigue estos pasos:

1. **Instalar Power BI Desktop y el Conector ODBC para SQLite**.
   - Descárgalo aquí Power BI Desktop: [https://powerbi.microsoft.com/desktop/](https://powerbi.microsoft.com/desktop/)
   - Descárgalo aquí el Conector ODBC (descarga la versión más actualizada): [http://www.ch-werner.de/sqliteodbc/](http://www.ch-werner.de/sqliteodbc/)

2. **Obtener una clave de API de YouTube V3** si planeas usarlo de forma recurrente, tienes las instrucciones en la opción 3 del menu.

3. **Ejecutar el archivo .exe** (doble clic sobre el archivo ejecutable).

4. **Ingresar la URL del canal de YouTube** cuando se solicite.

5. **Esperar** a que el programa descargue los datos y actualice automáticamente la presentación en Power BI.



## Instrucciones para programadores y desarrolladores

### Requisitos

1. **Power BI Desktop**: Debe estar instalado para actualizar las presentaciones.

   - Descárgalo aquí: [https://powerbi.microsoft.com/desktop/](https://powerbi.microsoft.com/desktop/)

2. **Conector ODBC para SQLite**: Necesario para que Power BI pueda conectarse a la base de datos SQLite.

   - Descárgalo aquí (descarga la versión más actualizada): [http://www.ch-werner.de/sqliteodbc/](http://www.ch-werner.de/sqliteodbc/)

3. **Python 3.x**: Para ejecutar los scripts de análisis, descarga de datos y actualización de la presentación.

   - Descárgalo aquí: [https://www.python.org/](https://www.python.org/)

4. **Bibliotecas Python necesarias**:

   - `pyautogui`: Para simular la tecla F5 y actualizar la presentación.
   - `googleapiclient.discovery`: Para interactuar con la API de YouTube.
   - `dotenv`: Para cargar claves API desde un archivo `.env`.
   - `requests`: Para realizar solicitudes HTTP.
   - `sqlite3`: Para manejar la base de datos.
   - `re`, `os`, `shutil`, `time`, `sys`: Para manipulación de archivos y control de flujo.

   Instala todas las bibliotecas con el siguiente comando:

   ```bash
   pip install -r requirements.txt
   ```

5. **Clave de API de YouTube**:

   - Si planeas usar el programa de forma recurrente, necesitas una clave API de YouTube V3, la cual es gratis y fácil de obtener.
   - Puedes obtenerla siguiendo las instrucciones en la opción **3 del menú** del programa.
   - Si solo realizarás unas pocas pruebas, no es necesario cambiar la clave de API.

### Instalación

1. **Instalar Python 3.x**
2. **Instalar las bibliotecas necesarias**
3. **Instalar Power BI y el conector de SQLite**
4. **Obtener una clave de API de YouTube** de ser necesario.

### Instrucciones

1. **Ejecutar el programa manualmente**:

   ```bash
   python main.py
   ```

2. **Interacción**:
   Cuando ejecutes el programa, se te presentará un menú con tres opciones:

   - **Opción 1**: Cambiar la clave de la API de YouTube (solo necesario si se usará con frecuencia).
   - **Opción 2**: Analizar un canal de YouTube y obtener los comentarios de los videos.
   - **Opción 3**: Instrucciones para obtener la clave de API.

3. **Proceso**:

   - Al elegir la **Opción 2**, el programa descargará la información del canal de YouTube que hayas ingresado, incluyendo los comentarios de los videos, y la guardará en la base de datos, para posteriormente ejecutar la presentación interactiva en Power BI.

## Licencia

Este proyecto está bajo la licencia MIT.

