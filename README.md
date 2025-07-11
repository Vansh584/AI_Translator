# AI-Powered Multi-Language Translator 🌍🗣️

This project is a web-based multi-language translator that uses Google Translate and Text-to-Speech (TTS) technologies to provide real-time translation and audio playback in various languages.

## 🚀 Features

- 🔤 Translate text between multiple languages.
- 🔊 Convert translated text to speech using `gTTS`.
- 🌐 Web frontend with HTML, CSS, and JavaScript.
- 🧠 AI logic in Python using `googletrans` and `gTTS`.

## 📁 Project Structure


## 🛠️ Setup Instructions

1. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` is missing, install manually:

    ```bash
    pip install flask googletrans==4.0.0-rc1 gTTS
    ```

3. **Run the app**:

    ```bash
    python app.py
    ```

4. **Open in browser**:

    Go to `http://127.0.0.1:5000`

## 🧠 Tech Stack

- **Backend**: Python, Flask
- **Translation**: `googletrans`
- **TTS**: `gTTS` (Google Text-to-Speech)
- **Frontend**: HTML, CSS, JavaScript

## 📌 Notes

- Make sure you have an active internet connection — both `googletrans` and `gTTS` require it.
- The translated audio is saved as `translated_audio.mp3`.

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).
