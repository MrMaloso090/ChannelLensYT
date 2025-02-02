def Key_Changer():
    
    from googleapiclient.discovery import build
    def Main():
        from ChannelLensYT import MainMenu
        MainMenu()


    #Definicion del mensaje de error.
    #Error Message definition.
    def Error_Message():
        print(f'''\033[31m
    ==================================================
                        ERROR  
    ==================================================\033[0m
    ==================================================
    Please try again and ensure the key is entered 
    correctly.
    ==================================================
    ''')
        input('\033[32mPress Enter\033[0m')
        Main()



    #Peticion de de la nueva API Key.
    #New API key request.
    print(f'''\033[32m
    ==================================================
                    API Key Changer
    ==================================================\033[0m
    ==================================================
    Enter your personal API key to personalize the 
    program and use it within your own credit limits.
    ==================================================  
    ''')
    New_key = input('\033[32mAPI Key: \033[0m')

    if len(New_key) == 0:
        print("\033[31mError: API Key cannot be empty.\033[0m")
        Error_Message()




    #Validacion de la API key
    #API key validation.
    try:
        youtube = build('youtube' , 'v3' , developerKey = New_key)
        request = youtube.channels().list(
            part = 'snippet',
            forUsername = 'Google' #Famous Chanel
        )
        answer = request.execute()
    except Exception as e:
        print(f"\033[31mUnexpected Error: {e}\033[0m")
        Error_Message()



    #Guardado de la nueva API.
    #New API save.
    try:
        with open('.env' , 'w') as f:
            f.write(f'API_KEY={New_key}\n')
    except Exception as e:
        print(f"\033[31mError saving API key to file: {e}\033[0m")
        Main()



    #Despedida
    #Farewell
    print(f'''\033[32m
    ==================================================
                    API key saved
    ==================================================\033[0m
    ''')


#Key_Changer()
#==================================================
#Code Author: Daniel Sanchez Velasquez - TakuSan.
#Email - daniel.sanchez.velasquez090@gmail.com
#GitHub - https://github.com/MrMaloso090
#==================================================