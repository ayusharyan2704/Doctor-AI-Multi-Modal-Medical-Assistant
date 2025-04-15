# 🧠 Doctor AI — Multi-Modal Medical Assistant

An intelligent **multi-modal AI system** that mimics how a real doctor communicates. Users can **speak** their symptoms and **upload an image**, and the bot will analyze the input using advanced **LLMs**, **vision models**, and **TTS synthesis** to deliver a **human-like medical voice response**.

## 🚀 Features

- 🎤 **Voice Input**: Speak symptoms directly to the system
- 🖼️ **Image Upload**: Upload medical images (e.g., rashes, X-rays)
- 🧠 **LLM + Vision Analysis**: Uses GROQ's LLaMA-3 Vision model for intelligent reasoning
- 🔊 **Text-to-Speech Response**: Responds with a lifelike medical voice using TTS
- 🔄 **Multi-modal Fusion**: Combines voice and visual context for a better diagnosis

---
## 🎥 Video Explanation

Here’s a brief video walkthrough of the **Doctor AI – Multi-Modal Medical Assistant**:

[![Doctor AI – Multi-Modal Medical Assistant Video](https://img.youtube.com/vi/mYvFn3bruvA/0.jpg)](https://www.youtube.com/watch?v=mYvFn3bruvA)

Click the image above to watch the full video!

---

## 🟩 Screenshots of responses(Text+Audio) :
![image](https://github.com/user-attachments/assets/6ef3b156-24f1-46a5-b098-5184deb7ca86)

![image](https://github.com/user-attachments/assets/eabb3021-73d6-4255-bf56-d1f35de3d69a)

![image](https://github.com/user-attachments/assets/f22020c0-77dd-42eb-87e5-b3f5cf530c5b)

---
## 🧠 Tech Stack Breakdown

A detailed view of all the technologies used in each phase of the AI Doctor Bot pipeline:

---

### 🟩 Phase 1 – Audio Recorder  
**Purpose:** Capture user voice input  

**Tech Stack:**
- **Gradio** – Interactive UI for microphone input  
- **Python** – Backend logic and orchestration  
- **Gradio.Audio** – Component to capture real-time audio  
- **WAV/MP3 File Handling** – Temporarily saves recorded audio  

---

### 🟦 Phase 2 – Speech-to-Text (STT)  
**Purpose:** Convert user’s spoken input into transcribed text  

**Tech Stack:**
- **Groq API** – Provides fast inference for AI models  
- **OpenAI Whisper (via Groq)** – Powerful STT AI model (`whisper-large-v3`)  
- **Python** – Handles API interaction and file operations  
- **dotenv (.env)** – Manages and secures API keys  

---

### 🟨 Phase 3 – Vision + LLM Response  
**Purpose:** Analyze uploaded medical images and generate diagnostic responses  

**Tech Stack:**
- **Meta's LLaMA Vision-Language Model** – Performs multimodal analysis (text + image)  
- **Groq API** – Delivers high-speed, low-latency LLM inference  
- **Base64 Encoding** – Prepares image data for processing  
- **Gradio.Image** – Handles image file uploads via UI  
- **Prompt Engineering** – Custom instructions to mimic a doctor’s tone  

---

### 🟥 Phase 4 – Text-to-Speech (TTS)  
**Purpose:** Convert AI-generated diagnosis into voice output  

**Tech Stack:**
- **ElevenLabs API** – Converts text into high-quality, human-like speech  
- **Python Requests** – Sends LLM output to ElevenLabs and fetches audio  
- **MP3 File Output** – Saves and returns audio response  
- **Gradio.Audio** – Plays back audio in the web interface  

---


## 🧪Example Flow

1. User clicks **mic** and speaks: “I have pain near my lower back.”
2. User uploads an image of the affected area.
3. AI processes voice + image.
4. Output:
   - **Text diagnosis** appears in chat.
   - **Audio response** plays automatically.


---
# Guide to Installation

1. Clone the repository:
   
     git clone https://github.com/ayusharyan2704/Doctor-AI-Multi-Modal-Medical-Assistant.git
   
     cd Doctor-AI-Multi-Modal-Medical-Assistant

2. Create and activate a virtual environment:
     ## On Windows
     python -m venv venv
   
     venv\Scripts\activate
   
     ## On Mac/Linux
     python -m venv venv
   
     source venv/bin/activate

4. Install the required dependencies:

   pip install -r requirements.txt

6. Configure Environment Variables:

   Create a .env file in the root directory.

   Add your keys:
   
     GROQ_API_KEY=your_groq_api_key
   
     ELEVENLABS_API_KEY=your_elevenlabs_api_key
   
7. Usage : Once the setup is complete, run python final.py

---



