import sqlite3
import os
import time
def Main():
    from ChannelLensYT import MainMenu
    MainMenu()



def Instructions_ODBC():
    #Coneccion SQL
    #SQL conection
    conn = sqlite3.connect('Temporal_DataBase.sqlite')
    cur = conn.cursor()

    #Borrado de las tablas anteriores.
    #Delete previous tables.
    cur.executescript('''
        DROP TABLE IF EXISTS Channel;
        DROP TABLE IF EXISTS Videos;
        DROP TABLE IF EXISTS Shorts;
        DROP TABLE IF EXISTS Videos_Comments;
        DROP TABLE IF EXISTS Shorts_Comments;
    ''')

    #Creacion de las tablas limpias.
    #Clean Tables Creation
    cur.executescript('''
        CREATE TABLE Channel(
            name,
            description,
            country,
            creation_date,
            subscribers,
            total_videos,
            total_views,
            image
        );
        CREATE TABLE Videos(
            id INTEGER PRIMARY KEY NOT NULL,
            titles,
            dates,
            views_count,
            likes_count,
            comments_count,
            durations,
            url,
            image,
            seconds
        );
        CREATE TABLE Shorts(
            id INTEGER PRIMARY KEY NOT NULL,
            titles,
            dates,
            views_count,
            likes_count,
            comments_count,
            durations,
            url,
            image,
            seconds
        );
        CREATE TABLE Videos_Comments(
            title_id INTEGER,
            subs,
            likes,
            comments,
            dates
        );
        CREATE TABLE Shorts_Comments(
            title_id INTEGER,
            subs,
            likes,
            comments,
            dates
        )
    ''')



    #Instrucciones.
    #Instructions.
    print(f'''
    \033[32m==========================================
    ChannelLensYT - Initial Setup Guide  
    ==========================================\033[0m

    If this is your first time using ChannelLensYT or you moved the folder, follow these steps once.  
    After that, you can use the program normally.  

    ------------------------------------------
    1. Install the ODBC Driver for SQLite  
    ------------------------------------------

    > DOWNLOAD:  
    - Go to \033[34mhttp://www.ch-werner.de/sqliteodbc/\033[0m
    - Download the **SQLite3 ODBC Driver** for Windows  
    - (Or find the appropriate version for your system)  

    > INSTALL:  
    - Run the downloaded file and follow the instructions  

    ------------------------------------------
    2. Configure the ODBC Data Source  
    ------------------------------------------

    > OPEN ODBC:  
    - Press `Win + S`, type **"ODBC"**, and open **"ODBC Data Source Administrator"**  

    > CREATE DATA SOURCE:  
    - Go to the **"User DSN"** tab  
    - Click **"Add"**  
    - Select **"SQLite3 ODBC Driver"**  
    - Assign a name (e.g., **"ChannelLensYT"**)  
    - Locate and select the **'Temporal_DataBase.sqlite'** file  
    - (It will be in the same folder as the executable `.exe`)  
    - Click **"OK"**  

    ------------------------------------------
    3. Update Tables in Power BI  
    ------------------------------------------

    > OPEN POWER BI:  
    - Select option `2` in the input below to open Power BI  

    > UPDATE TABLES:  
    - In the top menu, click **"Transform Data"**  
    - On the left panel, select each table one by one:  
        - `Channel`  
        - `Shorts`  
        - `Videos`  
        - `Shorts_Comments`  
        - `Videos_Comments`  
    - For each table, go to the right panel and find **'source'**  
    - Double-click, select the name you configured in ODBC (e.g., **"ChannelLensYT"**)  
    - In the pop-up window, select "Windows Authentication"
    - Leave the username and password fields blank
    - Click **OK**
    - Repeat for each table  

    > APPLY CHANGES:  
    - Click **"Close & Apply"** in the upper right corner  

    ------------------------------------------
    4. Save the Project  
    ------------------------------------------

    > SAVE & CLOSE:  
    - Press `Ctrl + S` or go to **File > Save**  
    - Close Power BI without modifying anything else  
    - This file will be used as a reference by the program  

    \033[32m==========================================
    
        Press 1 to go back to the menu.  
        Press 2 to open Power BI to make the changes.  
    ==========================================\033[0m
''')

    number = input('\033[32mEnter your choice: \033[0m')

    if number == '1':
        Main()

    elif number == '2':
        original_file = os.path.join(os.getcwd(), "_file", "ChannelLensYT.pbix")

        os.startfile(original_file)
        time.sleep(5)
        Main()

    else:
        print(f'''\033[31m
    ==================================================
                        ERROR  
    ==================================================\033[0m
    ==================================================
    Enter a valid option.
    ==================================================
        ''')
        time.sleep(1)
        Instructions_ODBC()



#==================================================
#Code Author: Daniel Sanchez Velasquez - TakuSan.
#Email - daniel.sanchez.velasquez090@gmail.com
#GitHub - https://github.com/MrMaloso090
#==================================================