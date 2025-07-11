from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
from googletrans import Translator
import googletrans
from gtts import gTTS
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)  

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/languages')
def get_languages():
    return jsonify(googletrans.LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text_to_translate')
    source_language_code = data.get('source_language_input')
    target_language_code = data.get('target_language_input')

    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language_code, src=source_language_code or 'auto')
        translatedText = translation.text

        audio_path = "static/translated_audio.mp3"
        tts = gTTS(text=translatedText, lang=target_language_code)
        tts.save(audio_path)

        return jsonify({
        'translatedText': translatedText,
        'audioUrl': '/' + audio_path
    })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/static/<filename>')
def serve_audio(filename):
    return send_file(os.path.join('static', filename), mimetype='audio/mpeg')

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)
