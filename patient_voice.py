# ==================== LOAD ENV =====================
from dotenv import load_dotenv
import os
load_dotenv()
from pydub import AudioSegment
from pydub.utils import which
from io import BytesIO

# Set path to ffmpeg manually (update if needed)
AudioSegment.converter = r"C:\ffmpeg\ffmpeg-2025-04-14-git-3b2a9410ef-full_build\bin\ffmpeg.exe"


# ==================== IMPORTS ======================
import logging
import speech_recognition as sr
from groq import Groq

# ==================== LOGGING SETUP =================
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ==================== CONFIG =======================
audio_filepath = "patient_voice_test.mp3"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
stt_model = "whisper-large-v3"

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found. Please check your .env file.")

# ==================== AUDIO RECORDING FUNCTION =======================
def record_audio(file_path, timeout=20, phrase_time_limit=30):
    """Records audio from the microphone and saves it as an MP3 file."""
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("🎙️ Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("🗣️ Start speaking...")
            
            # Record
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("✅ Recording complete.")
            
            # Convert to MP3
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"💾 Audio saved to: {file_path}")

    except Exception as e:
        logging.error(f"❌ Error during recording: {e}")

# ==================== TRANSCRIPTION FUNCTION =======================
def transcribe_with_groq(model, file_path, api_key):
    """ Sends audio file to Groq STT and returns the transcript. """
    try:
        client = Groq(api_key=api_key)

        with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model=model,
                file=audio_file,
                language="en"
            )
        return transcription.text
    except Exception as e:
        logging.error(f"❌ Error during transcription: {e}")
        return None

# ==================== MAIN RUN =======================
if __name__ == "__main__":
    # Step 1: Record Audio
    record_audio(file_path=audio_filepath)
    
    # Step 2: Check if the audio file exists before transcription
    if os.path.exists(audio_filepath):
        transcript = transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY)
        
        if transcript:
            print("\n🧾 Transcript from patient:")
            print(transcript)
        else:
            print("\n⚠️ No transcript available.")
    else:
        print(f"⚠️ Audio file not found: {audio_filepath}. Please check your microphone and recording settings.")
