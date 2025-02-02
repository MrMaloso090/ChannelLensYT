def Data_Downloader():

    from googleapiclient.discovery import build
    from dotenv import load_dotenv
    import os
    import re
    import sqlite3
    import requests
    def Main():
        from ChannelLensYT import MainMenu
        MainMenu()

    #RECUPERACION DE LA APY_KEY GUARDADA en .env
    #RECOVERING THE SAVED APY_KEY FROM .env
    load_dotenv()
    API_key = os.getenv('API_KEY')

    #Coneccion con la API.
    #API conection.
    youtube = build('youtube', 'v3', developerKey= API_key )

    #Definicion del mensaje de error.
    #Error Message definition.
    def Error_Message():
        print(f'''\033[31m
    ==================================================
                        ERROR  
    ==================================================\033[0m
    ==================================================
    Please try again and ensure the YouTube channel 
    URL is entered correctly.
    ==================================================
    ''')
        input('\033[32mPress Enter\033[0m')
        Main()

    #Menu del buscador.
    #Sercher menu.
    print(f'''\033[32m
    ==================================================
                    Channel Finder
    ==================================================\033[0m
    ==================================================
    Enter the URL of the channel you want to analyze. 
    It will be the link displayed on the account's 
    main page.
    ==================================================  
    ''')
    Channel_URL = input('\033[32mChannel URL: \033[0m')

    if len(Channel_URL) == 0:
        print("\033[31mError: Channel URL cannot be empty.\033[0m")
        Error_Message()

    #Filtro para las URLs que no son de youtube.
    #Filter for non youtube URLs
    if not 'youtube.com' in Channel_URL:
        print("\033[31mError: The URL doesn't appear to be from youtube.com.\033[0m")
        Error_Message()


    if not re.match((r'^(https?://)?(www\.)?youtube\.com(/.+)?$') , Channel_URL):
        print("\033[31mError: The URL is not in the correct format or does not include the channel.\033[0m")
        Error_Message()

    #Filtro para los 4 tipos de URL posibles.
    #Filter for the 4 possible types of URLs
    if '/channel/' in Channel_URL:
        Channel_ID = Channel_URL.split('/channel/')[1].split('/')[0]


    elif '/c/' in Channel_URL or '/user/' in Channel_URL or '/@' in Channel_URL:
        x = re.split(r'/c/|/user/|/@',Channel_URL)[1]
        Usar_Name = x.split('/')[0]


    else:
        print("\033[31mError: The URL does not match the main page of a channel.\033[0m")
        Error_Message()

    #Busuqueda del ID si es necesario.
    #ID serch if necessary
    if Usar_Name != None:
        request = youtube.search().list(
        part = 'snippet',
        q = Usar_Name,
        type = 'channel',
        maxResults = 1,
        )
        answer = request.execute()

        try:
            Channel_ID = answer['items'][0]['id']['channelId']
        except Exception as e:
            print(f"\033[31mError: {e}\033[0m")
            print(f"\033[31mUsername chanel not found.\033[0m")
            Error_Message()

    #Mensage de aprobacion.
    #Aprove message.
    print(f'''\033[32m
    ==================================================
                    Data Downloading
    ==================================================\033[0m
    ==================================================
    Wait until the process is complete.
    ...
    ==================================================  
    ''')

    #Obtension de la informacion del canal, y su playlist ID
    #Getting channel information, and its playlist ID
    request = youtube.channels().list(
        part = 'snippet,statistics,contentDetails',
        id = Channel_ID
    )
    answer = request.execute()


    Channel_Information = answer['items'][0]

    PlayList_ID = Channel_Information.get('contentDetails', {}).get('relatedPlaylists', {}).get('uploads', None)
    if PlayList_ID == None:
        print(f"\033[31mIt seems this channel doesn't have an available playlist.\033[0m") #Error for channel with no videos.
        Error_Message()    

    ChannelName = Channel_Information['snippet'].get('title' , '') #Important <====================
    ChannelDescription = Channel_Information['snippet'].get('description' , '') #Important <====================
    ChannelImage = Channel_Information['snippet'].get('thumbnails' , {}).get('high' , {}).get('url' , '') #Important <====================
    ChannelCreationDate =  Channel_Information['snippet'].get('publishedAt' , '')[:10] #Important <====================
    ChannelSubscribers = Channel_Information['statistics'].get('subscriberCount', '') #Important <====================
    ChannelVideosCount = Channel_Information['statistics'].get('videoCount', '') #Important <====================
    ChannelTotalViews = Channel_Information['statistics'].get('viewCount', '') #Important <====================
    ChannelCountry = Channel_Information['snippet'].get('country', '') #Important <====================

    #Optencion de los datos basico del video y si video ID (parabuscar informacion extra)
    #Obtaining basic video data and its video ID (to search for extra information)
    VideosIDs_list = list()
    VideoTitles_list = list() #Important <====================
    VideosURLs_list = list() #Important <====================
    VideosDates_list = list() #Important <====================

    NextPage_token = None
    while True:
        request = youtube.playlistItems().list(
            part = 'snippet',
            playlistId = PlayList_ID,
            maxResults = 50,
            pageToken = NextPage_token
        )
        answer = request.execute()

        for data in answer.get('items' , []):
            title = data['snippet'].get('title' , '')
            id = data['snippet'].get('resourceId', {}).get('videoId' , '')
            url = f'https://www.youtube.com/watch?v={id}'
            date = data['snippet'].get('publishedAt' , '')

            VideosIDs_list.append(id)
            VideoTitles_list.append(title)
            VideosURLs_list.append(url)
            VideosDates_list.append(date[:10])
        

        NextPage_token = answer.get('nextPageToken') #If this exist means the channel have more than 50 videos(Max API download), and create a loop to download all, until ther is not more pages.

        if not NextPage_token:
            break

    #Obtencion de los datos extra del video
    #Getting extra data from the video
    VideosViews_list = list() #Important <====================
    VideosLikes_list = list() #Important <====================
    VideosDuration_list = list() #Important <====================
    VideoImage_list = list() #Important <====================
    VideoComments_list = list() #Important <====================


    for data in VideosIDs_list:

        request = youtube.videos().list(
            part = 'snippet,statistics,contentDetails,status',
            id = data,
        )
        answer = request.execute()


        Extra_Information = answer['items'][0]

        views = Extra_Information['statistics'].get('viewCount', '')
        likes = Extra_Information['statistics'].get('likeCount', '')
        duration =  Extra_Information['contentDetails'].get('duration' , '')
        image = Extra_Information['snippet'].get('thumbnails' , {}).get('high' , {}).get('url' , '')
        comments = Extra_Information['statistics'].get('commentCount', '0')


        VideosViews_list.append(views)
        VideosLikes_list.append(likes)
        VideosDuration_list.append(duration)
        VideoImage_list.append(image)
        VideoComments_list.append(comments)

    #Transcripcion de las duraciones.
    #Transcription of durations
    durations = list() #IMPORTANT <====================
    seconds_list = list() #IMPORTANT <====================

    for data in VideosDuration_list:
        hours = re.findall(r'PT(\d+)H(?:\d+M)?(?:\d+S)?' , data)
        minutes = re.findall(r'PT(?:\d+H)?(\d+)M(?:\d+S)?' , data)
        seconds = re.findall(r'PT(?:\d+H)?(?:\d+M)?(\d+)S' , data)

        def chek(x):
            if not x:
                y = '00'
            else:
                y = x[0]
            if len(y) == 1:
                y = f'0{y}'
            return y
        
        hours = chek(hours)
        minutes = chek(minutes)
        seconds = chek(seconds)

    #    if hours != '00':
    #        duration_ = f'{hours}:{minutes}:{seconds}'
    #    else:
    #        duration_ = f'{minutes}:{seconds}'
        duration_ = f'{hours}:{minutes}:{seconds}'

        total_seconds = int(hours) * 60
        total_seconds = (int(minutes) + total_seconds) * 60
        total_seconds = int(seconds) + total_seconds

        durations.append(duration_)
        seconds_list.append(total_seconds)

    #Guardado de todos los datos optenidos dentro de la base de datos. #############################################################################################################################################
    #Saving all data obtained within the database. #################################################################################################################################################################

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

    #Guardado de datos del canal.
    #Chanel data save.
    cur.execute('''
        INSERT INTO Channel (name, description, country, creation_date, subscribers, total_videos, total_views, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        (ChannelName, ChannelDescription, ChannelCountry, ChannelCreationDate, ChannelSubscribers, ChannelVideosCount, ChannelTotalViews, ChannelImage))
    conn.commit()

    #Guardardado de datos de los videos y shorts.
    #Saving videos and shorts data.
    for x in range(len(VideoTitles_list)):
        
        #Filtro de videos o shorts.
        #Videos or shorts filter.
        URL_filter = f'https://www.youtube.com/shorts/watch?v={VideosIDs_list[x]}'
        answer = requests.get(URL_filter, allow_redirects=True)
        print(VideosIDs_list[x])

        if answer.url != URL_filter:
            cur.execute('''
                INSERT INTO Videos(titles, dates, views_count, likes_count, comments_count, durations, url, image, seconds)
                VALUES (?,?,?,?,?,?,?,?,?)''',
                (VideoTitles_list[x], VideosDates_list[x], VideosViews_list[x], VideosLikes_list[x], VideoComments_list[x], durations[x], VideosURLs_list[x], VideoImage_list[x], seconds_list[x]))
        else:
            cur.execute('''
                INSERT INTO Shorts(titles, dates, views_count, likes_count, comments_count, durations, url, image, seconds)
                VALUES (?,?,?,?,?,?,?,?,?)''',
                (VideoTitles_list[x], VideosDates_list[x], VideosViews_list[x], VideosLikes_list[x], VideoComments_list[x], durations[x], VideosURLs_list[x], VideoImage_list[x], seconds_list[x]))
    conn.commit()

    #Cierre.
    #Close.
    conn.close()

    #Mensage final del rpoceso descarga.
    #Final message of the download process.
    print(f'''\033[32m
    ==================================================
                Data Successfully Downloaded
    ==================================================\033[0m
    ==================================================
    Continue waiting until the process is complete.
    ...
    ==================================================  
    ''')


#Data_Downloader()
#==================================================
#Code Author: Daniel Sanchez Velasquez - TakuSan.
#Email - daniel.sanchez.velasquez090@gmail.com
#GitHub - https://github.com/MrMaloso090
#==================================================