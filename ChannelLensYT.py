def MainMenu():

    import os
    import shutil
    import pyautogui
    import time
    import sys

    from Key_Changer import Key_Changer
    from Data_Downloader import Data_Downloader
    from Complement_Comments import Comments
    from Instructions_ODBC import Instructions_ODBC

    #Protocolo.
    #Protocol.
    print(f'''\033[33m
    ==================================================
                Press Enter to Continue
    ==================================================\033[0m
    ''')
    input('\033[33mPress Enter\033[0m')

    #Introduccion.
    #Intrduction.
    print(f'''\033[32m
    ==================================================
                    ChannelLensYT
    ==================================================\033[0m
    ==================================================
    Please, if you wish to use this program on a 
    recurring basis, I ask that you obtain your own 
    free Google Cloud YouTube V3 API key. It is easy to 
    get and will allow you to analyze a large number of 
    videos. This way, you will respect the usage limit 
    of my key, and I wont have to disable it. 
    Thank you for your understanding!
    ==================================================
    \033[32mTo use this program you will need to:
    Install Power BI Desktop and the SQLite ODBC Connector.\033[0m
    Download Power BI Desktop: \033[34mhttps://powerbi.microsoft.com/desktop/\033[0m
    Download ODBC (latest version): \033[34mhttp://www.ch-werner.de/sqliteodbc/\033[0m
    ==================================================

            Press 1 to change the API key.
            Press 2 to analyze a YouTube channel.
                Press 3 if this is your first time using the program, follow these steps!
            Press 4 to get instructions on how to obtain the API key
    ==================================================
    ''')

    number = input('\033[32mEnter your choice: \033[0m')


    #Cambio de API key.
    #API key changer.
    if number == '1':
        Key_Changer()
        MainMenu()


    #Ejecucion del programa.
    #Program execution.
    elif number == '2':
        Data_Downloader()
        #Uso de la definicion del codigo Complement_Comments
        #Uses of the definition from Complement_comments
        Comments('videos', 'Videos_Comments')
        Comments('Shorts', 'Shorts_Comments')

        #Purga de archivo con posibilidad de corrupcion.
        #File purge with potential for corruption.
        if os.path.exists('ChannelLensYT.pbix'):
            os.remove('ChannelLensYT.pbix')
            time.sleep(1)

        #Renovacion de la presentacion.
        #Presentation renewal.
        original_file = os.path.join(os.getcwd(), "_file", "ChannelLensYT.pbix")
        actual_path = os.getcwd()

        shutil.copy(original_file, actual_path)
        time.sleep(1)

        #Ejecucion y actualizacion de la presentacion.
        #Presentation executionand update.
        print(f'''\033[32m
    ==================================================
    If the presentation does not refresh automatically:
    ==================================================\033[0m
    ==================================================
    Click Refresh in the top panel.
    (Home / Refresh)
    ==================================================
    ''')
        time.sleep(2)

        os.startfile('ChannelLensYT.pbix')
        time.sleep(20)

        pyautogui.hotkey("f5")

        time.sleep(1)
        sys.exit()
    
    #Primer Paso.
    #First step.
    elif number == '3':
        Instructions_ODBC()

    #Instrucciones.
    #Instructions.
    elif number == '4':
        print(f'''\033[32m
    ====================================================================================================
                                    Instructions to Obtain Your API Key 
    ====================================================================================================\033[0m
    ====================================================================================================
    1. Access the Google Developers Console: Log in with your Google account at 
        \033[34mhttps://console.developers.google.com/\033[0m

    2. Create a new project: Click on the project dropdown menu at the top and select "New Project". 
        Give your project a name and click "Create".

    3. Enable the YouTube Data API v3:
    - In the left navigation panel, select "Library".
    - Search for "YouTube Data API v3" in the search bar.
    - Click on "YouTube Data API v3" and then click "Enable".

    4. Create the credentials:
    - After enabling the API, click on "Create Credentials".
    - In "Which API are you using?", select "YouTube Data API v3".
    - In "Where will you be calling the API from?", choose "Web server (e.g., node.js, Tomcat)".
    - In "What data will you access?", select "Public data".
    - Click on "What credentials do I need?".
    - On the next screen, select "API Key" and click "Create".

    5. Get your API key: Once created, your API key will be displayed. Copy it and keep it in a safe 
        place, as you will need it to authenticate your requests to the YouTube API.
    ====================================================================================================
    ''')
        MainMenu()


    #Error opcion invalida.
    #Error invalid option.
    else:
        print(f'''\033[31m
    ==================================================
                        ERROR  
    ==================================================\033[0m
    ==================================================
    Enter a valid option.
    ==================================================
    ''')
        MainMenu()

#Ejecucion del codigo Main.
#Main Code Run.
print(f'''\033[3m
==================================================
Code Author: Daniel Sanchez Velasquez - TakuSan.
Email - daniel.sanchez.velasquez090@gmail.com
GitHub - \033[34mhttps://github.com/MrMaloso090\033[0m
\033[3m==================================================\033[0m
''')
 


MainMenu()
#==================================================
#Code Author: Daniel Sanchez Velasquez - TakuSan.
#Email - daniel.sanchez.velasquez090@gmail.com
#GitHub - https://github.com/MrMaloso090
#==================================================