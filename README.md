# HinglishColdCallingAgent

## Introduction
Hey there! 👋 Welcome to the **AI Cold Calling Agent**—a smart, interactive tool designed to make business calls sound more natural and engaging. This AI-powered assistant can hold **Hinglish** conversations for:

1. **Demo Scheduling** – Helping schedule product demos effortlessly.
2. **Candidate Interviews** – Conducting initial screening interviews like a pro.
3. **Payment Follow-ups** – Reminding customers about pending payments or new orders.

This project blends **OpenAI’s GPT model** with **voice support (TTS & STT)** and has a simple, easy-to-use **Streamlit UI** for interactions. 🚀

---

## Why You’ll Love This Project
✅ **Natural-Sounding Conversations** (Hinglish Support)  
✅ **Context-Aware AI Responses**  
✅ **Talk & Listen with Voice Features**  
✅ **Easy Web Interface with Streamlit**  
✅ **Future-Ready with CRM & Payment Integrations**  

---

## Getting Started
### 1️⃣ **Clone This Project**
First, grab a copy of this repository:
```bash
git clone https://github.com/your-repo-name.git
cd AI-Cold-Calling-Agent
```

### 2️⃣ **Set Up Your Environment** (Optional, but recommended)
```bash
python -m venv env
# Activate the environment:
# On Windows:
env\Scripts\activate

```

### 3️⃣ **Install Dependencies**
We’ve kept things simple—just run:
```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Your OpenAI API Key**
You need an API key from [OpenAI](https://platform.openai.com/). Once you have it, set it up:
```bash
# Windows (Command Prompt)
set OPENAI_API_KEY=your_api_key_here

```

---

## Running the App 🎯
Start the **Streamlit web interface** with:
```bash
python -m streamlit run main_script.py
```
This will open the app in your browser at:
```
http://localhost:8501
```

---

## Troubleshooting 🛠️
### **1️⃣ FFmpeg Issues?**
- Make sure **FFmpeg** is installed and added to your system PATH.
- Download it from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
- After installing, check if it works:
  ```bash
  ffmpeg -version
  ```

### **2️⃣ Permission Denied Errors?**
- Try **running VS Code as Administrator**.
- If the temp directory is causing issues, change it in `text_to_speech()`.

### **3️⃣ No Audio Output?**
- Check if your **speakers are on**.
- Modify `text_to_speech()` to **save in WAV format** instead of MP3.

---

## What’s Next? 🚀
🔹 **Integration with WhatsApp & Telegram** for messaging  
🔹 **More accurate speech recognition using Whisper API**  
🔹 **Deploying on AWS/GCP for real-world use**  

---

## Want to Contribute? 🤝
Love this project? Help make it better! Feel free to **fork, modify, and submit a pull request**. Got ideas? Open an issue and let’s discuss! 

---


