import streamlit as st
import openai
import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
import tempfile


AudioSegment.converter = r"C:\Users\BHAWNA KANSAL\Downloads\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe"
# Load API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Define AI Agent
class ConversationalAgent:
    def __init__(self):
        self.prompts = {
            "demo_scheduling": "Namaste {name}, hum {company} se bol rahe hain. {product} demo schedule karna chahenge. Aapke liye kaunsa time suitable hoga?",
            "candidate_interviewing": "Namaste, {company} se bol raha hoon. {role} interview start karte hain. Aap apne baare mein batayein?",
            "payment_followup": "Namaste {name}, aapka order #{order_id} ka payment ₹{amount} abhi pending hai. Kya aap iska status confirm kar sakte hain?"
        }

    def generate_response(self, scenario, context):
        system_prompt = {
            "demo_scheduling": "You are a polite sales representative speaking in Hinglish.",
            "candidate_interviewing": "You are a professional HR interviewer speaking in Hinglish.",
            "payment_followup": "You are a courteous accounts representative handling payment follow-ups."
        }.get(scenario, "You are a helpful assistant.")
        
        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": context}
                ],
                temperature=0.7,
                max_tokens=150
            )
            return res.choices[0].message['content'].strip()
        except Exception as e:
            return "Kuch technical problem hai, baad mein try karein."

# Speech-to-Text Function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source, timeout=5)
    try:
        return recognizer.recognize_google(audio, language="hi-IN")
    except:
        return ""

# Text-to-Speech Function
def text_to_speech(text,lang='hi'):
    if not text:
        return None

    temp_dir = os.path.join(os.getcwd(), "temp_audio")
    os.makedirs(temp_dir, exist_ok=True)

    mp3_filename = os.path.join(temp_dir, "output.mp3")
    wav_filename = os.path.join(temp_dir, "output.wav")  

    tts = gTTS(text=text, lang=lang)
    tts.save(mp3_filename)

    # Convert MP3 to WAV before playing
    audio = AudioSegment.from_file(mp3_filename, format="mp3")
    audio.export(wav_filename, format="wav")  # Convert to WAV
    play(AudioSegment.from_wav(wav_filename))

    return wav_filename

# Streamlit UI
st.title("AI Cold Calling Agent")
scenario = st.selectbox("Select Scenario:", ["demo_scheduling", "candidate_interviewing", "payment_followup"])
name = st.text_input("Enter Customer/Candidate Name:")
company = st.text_input("Enter Company Name:")
product = st.text_input("Enter Product Name (if applicable):")
role = st.text_input("Enter Role (if applicable):")
order_id = st.text_input("Enter Order ID (if applicable):")
amount = st.number_input("Enter Amount (if applicable):", min_value=0, step=500)

if st.button("Start Conversation"):
    agent = ConversationalAgent()
    initial_prompt = agent.prompts.get(scenario, "").format(name=name, company=company, product=product, role=role, order_id=order_id, amount=amount)
    st.write("AI:", initial_prompt)
    text_to_speech(initial_prompt)
    
    user_input = st.text_input("Your Response:")
    if user_input:
        response = agent.generate_response(scenario, user_input)
        st.write("AI:", response)
        text_to_speech(response)

        

