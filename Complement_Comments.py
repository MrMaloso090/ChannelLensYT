def Comments(TABLE, TABLE2):

    from googleapiclient.discovery import build
    import sqlite3
    from dotenv import load_dotenv
    import os
    from bs4 import BeautifulSoup

    #RECUPERACION DE LA APY_KEY GUARDADA en .env
    #RECOVERING THE SAVED APY_KEY FROM .env
    load_dotenv()
    API_key = os.getenv('API_KEY')

    #Coneccion con la API.
    #API conection.
    youtube = build('youtube', 'v3', developerKey= API_key )

    #Coneccion con la base de datos.
    #Data base connection.
    conn = sqlite3.connect('Temporal_DataBase.sqlite')
    cur = conn.cursor()

    #Recuperacion de los titulos y sus URLs
    #Recovering title and URLs
    cur.execute(f'SELECT url, titles FROM {TABLE}')
    full_data = cur.fetchall()

    #Obtencion de los comentarios para cada titulo.
    #Obteining comments from all titles.
    for x in full_data:
        ID = x[0][32:]
        title = x[1]
        print(f'Check:{ID}')

        #Recuperacion del id del titulo
        #Title id recovered.
        cur.execute(f'SELECT id FROM {TABLE} WHERE titles = ?', (title,))
        title_id = cur.fetchone()

        #Interaccion con la API
        #Interacting whit API
        request = youtube.commentThreads().list(
        part = 'snippet',
        videoId = ID,
        maxResults = 100,
        order = 'relevance',
        )
        answer = request.execute()

        for data in answer.get('items' , []):
            comment = data.get('snippet', {}).get('topLevelComment', {}).get('snippet', {}).get('textDisplay', '')
            sub = data.get('snippet', {}).get('topLevelComment', {}).get('snippet', {}).get('authorDisplayName', '')
            likes = data.get('snippet', {}).get('topLevelComment', {}).get('snippet', {}).get('likeCount', '0')
            date = data.get('snippet', {}).get('topLevelComment', {}).get('snippet', {}).get('publishedAt', '')

            comment = BeautifulSoup(comment, 'html.parser').get_text()

            #Guardado en la base de datos por cada titulo.
            #Saving in the database each title.
            cur.execute(f'''
                INSERT INTO {TABLE2}(title_id, subs, likes, comments, dates) VALUES (?, ?, ?, ?, ?)''',
                (title_id[0], sub, likes, comment, date))
            
    #Guardado
    #Save
    conn.commit()


#Comments()
#==================================================
#Code Author: Daniel Sanchez Velasquez - TakuSan.
#Email - daniel.sanchez.velasquez090@gmail.com
#GitHub - https://github.com/MrMaloso090
#==================================================