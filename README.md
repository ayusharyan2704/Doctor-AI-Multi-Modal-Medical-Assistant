# 🧠 Doctor AI — Multi-Modal Medical Assistant

An intelligent **multi-modal AI system** that mimics how a real doctor communicates. Users can **speak** their symptoms and **upload an image**, and the bot will analyze the input using advanced **LLMs**, **vision models**, and **TTS synthesis** to deliver a **human-like medical voice response**.

## 🚀 Features

- 🎤 **Voice Input**: Speak symptoms directly to the system
- 🖼️ **Image Upload**: Upload medical images (e.g., rashes, X-rays)
- 🧠 **LLM + Vision Analysis**: Uses GROQ's LLaMA-3 Vision model for intelligent reasoning
- 🔊 **Text-to-Speech Response**: Responds with a lifelike medical voice using TTS
- 🔄 **Multi-modal Fusion**: Combines voice and visual context for a better diagnosis

---

## 🛠️ Tech Stack

## 🧠 Tech Stack

| Feature            | Technology Used             |
|--------------------|-----------------------------|
| 🎤 Audio Input     | Gradio                      |
| 🗣️ Speech-to-Text (STT) | OpenAI Whisper via Groq     |
| 👁️ Vision + LLM     | Meta LLaMA + Groq            |
| 🗣️ Text-to-Speech (TTS) | ElevenLabs                  |
| 🖼️ UI Framework     | Gradio                      |

---

## Screenshots of responses(Text+Audio) :
![image](https://github.com/user-attachments/assets/6ef3b156-24f1-46a5-b098-5184deb7ca86)

![image](https://github.com/user-attachments/assets/eabb3021-73d6-4255-bf56-d1f35de3d69a)

![image](https://github.com/user-attachments/assets/f22020c0-77dd-42eb-87e5-b3f5cf530c5b)

## Installation

1. Clone the repository:
     git clone https://github.com/ayusharyan2704/Doctor-AI-Multi-Modal-Medical-Assistant.git
     cd Doctor-AI-Multi-Modal-Medical-Assistant

2. Create and activate a virtual environment:
     python -m venv venv
     # On Windows
     venv\Scripts\activate
     # On Mac/Linux
     source venv/bin/activate

3. Install the required dependencies:
     pip install -r requirements.txt

4. Configure Environment Variables:
     Create a .env file in the root directory.

    Add your keys:
     GROQ_API_KEY=your_groq_api_key
     ELEVENLABS_API_KEY=your_elevenlabs_api_key
5. Usage : Once the setup is complete, run python final.py
   
The app will launch in your browser using Gradio.

Speak into the microphone and/or upload an image (e.g., rash, x-ray).

The model will analyze inputs using LLaMA-3 Vision + Whisper and respond using ElevenLabs TTS.

