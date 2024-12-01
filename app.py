from flask import Flask, render_template, request, jsonify

import yt_dlp
from youtubesearchpython import VideosSearch

app = Flask(__name__)


@app.route('/')
def index():
    return 'hola mundo'



@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    search_query = data['search_query']
    videos_search = VideosSearch(search_query, limit=2)
    try:
        query_result = videos_search.result()
        video_link = query_result['result'][0]['link']
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_link])
        return jsonify({'message': 'Descarga completada exitosamente.'})
    except Exception as e:
        return jsonify({'message': f'Ocurrió un error: {e}'})
    

@app.route('/pruebita', methods=['GET'])
def pruebita():
    search_query = 'Pokemon sun and moon champion battle theme'
    videos_search = VideosSearch(search_query, limit=2)
    try:
        query_result = videos_search.result()
        video_link = query_result['result'][0]['link']
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_link])
        return jsonify({'message': 'Descarga completada exitosamente.'})
    except Exception as e:
        return jsonify({'message': f'Ocurrió un error: {e}'})
    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 