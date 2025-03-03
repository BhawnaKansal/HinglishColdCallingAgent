# HinglishColdCallingAgent

## Overview
The **Hinglish Cold Calling Agent** is a voice-based assistant designed to conduct natural and engaging business calls in Hinglish. It supports multiple scenarios such as:

- **Demo Scheduling** – Assisting with scheduling product demos.
- **Candidate Interviewing** – Conducting initial screening interviews.
- **Payment Follow-ups** – Reminding customers about pending payments.

This agent utilizes **OpenAI's GPT model** for intelligent responses, **Speech-to-Text (STT)** for voice input, and **Text-to-Speech (TTS)** for generating audio replies.

---

## Features
✅ **Human-like conversations** in Hinglish  
✅ **Voice-enabled interactions** (speech-to-text & text-to-speech)  
✅ **Smart AI-driven responses** with OpenAI GPT-3.5  
✅ **Streamlit web-based interface** for easy interaction  

---

## Installation
### 1. **Clone the Repository**
```bash
git clone https://github.com/your-repo-name.git
cd AI-Cold-Calling-Agent
```

### 2. **Set Up a Virtual Environment (Optional but Recommended)**
```bash
python -m venv env
# Activate the environment:
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### 3. **Install Required Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Set Up OpenAI API Key**
Get your OpenAI API key from [OpenAI](https://platform.openai.com/) and set it as an environment variable:
```bash
# Windows (Command Prompt)
set OPENAI_API_KEY=your_api_key_here

# macOS/Linux
export OPENAI_API_KEY=your_api_key_here
```

---

## Running the Application
### **Start the Streamlit Web Interface**
```bash
streamlit run ai_cold_calling.py
```
This will launch the app in your browser at:
```
http://localhost:8501
```

---

## Troubleshooting
### **1. Issues with Speech Recognition?**
- Ensure your **microphone** is connected and working.
- Run Streamlit as **Administrator** on Windows.

### **2. No Audio Output?**
- Check if your **speakers are on**.
- Modify `text_to_speech()` to **use a different audio format** if needed.

### **3. OpenAI API Key Issues?**
- Make sure you have a **valid API key**.
- If exceeding rate limits, try **reducing the request frequency**.

---

## Future Enhancements
🚀 Integration with **WhatsApp & Telegram** for messaging  
🚀 Improved **speech recognition accuracy** using Whisper API  
🚀 Deployment on **cloud services** (AWS/GCP)  

---

## Contributing
If you’d like to contribute, feel free to fork this repo and submit a **pull request**. If you have any feature requests, open an **issue**.

---





