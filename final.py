from dotenv import load_dotenv
load_dotenv()

import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_with_query
from patient_voice import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs

# ==================== SYSTEM PROMPT ====================
system_prompt = """You have to act as a professional doctor, I know you are not, but this is for learning purposes.
What's in this image? Do you find anything wrong with it medically?
If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in
your response. Your response should be in one long paragraph. Also, always answer as if you are answering to a real person.
Do not say 'In the image I see' but say 'With what I see, I think you have ....'
Don't respond as an AI model in markdown; your answer should mimic that of an actual doctor, not an AI bot,
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

# ==================== MAIN PROCESSING FUNCTION ====================

def process_inputs(audio_filepath, image_filepath):
    # Step 1: Transcribe speech
    speech_to_text_output = transcribe_with_groq(
        model="whisper-large-v3",
        file_path=audio_filepath,
        api_key=os.getenv("GROQ_API_KEY")
    )

    # Step 2: Analyze image if provided
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided for me to analyze"

    # Step 3: Generate voice output
    audio_output_path = "final.mp3"
    text_to_speech_with_elevenlabs(
        input_text=doctor_response,
        output_filepath=audio_output_path
    )

    #  Return audio file path for Gradio to use
    return speech_to_text_output, doctor_response, audio_output_path


iface = gr.Interface(
    fn=process_inputs,
    inputs=[ 
        gr.Audio(sources=["microphone"], type="filepath", label="Speak to the Doctor"),
        gr.Image(type="filepath", label="Upload Image (optional)")
    ],
    outputs=[ 
        gr.Textbox(label="Transcribed Speech"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(type="filepath", label="Doctor's Voice Response")  
    ],
    title="🩺 AI Doctor - Speech to Diagnosis"
)

iface.launch(debug=True)
