import yt_dlp
from youtubesearchpython import VideosSearch

# Buscar videos en YouTube
search_query = 'pokemon championship ost sun and moon'
videos_search = VideosSearch(search_query, limit=2)

try:
    # Obtener el enlace del primer resultado
    query_result = videos_search.result()
    video_link = query_result['result'][0]['link']
    print(f"Video encontrado: {video_link}")

    # Configuración para descargar solo el audio sin postprocesamiento
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    # Descargar el audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])
    print("Descarga completada exitosamente.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
