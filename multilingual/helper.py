import speech_recognition as sr
from langchain_groq import ChatGroq
import os
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
groq_api_key=os.getenv("GROQ_API_KEY")

def voice_input():#converts speech to text:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio=recognizer.listen(source,timeout=5)

    try:    
        text=recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
            print(f"API error: {e}")
    

def text_to_speeh(text):
    tts=gTTS(text=text,lang="en")
    tts.save("speech.mp3")

def llm_model_object(user_text):
    model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

    generic_template="You are name is Rispah and you are an advanced multilingual AI assistant created to assist users seamlessly using various languages, cultures, and contexts. You are highly fluent in English, Tamil,Spanish, French, German, Chinese, Hindi, Arabic, Japanese, Portuguese, Russian, and other major languages. Your primary goal is to provide accurate, relevant, and contextually appropriate responses while ensuring a user-friendly experience"
    
    prompt=ChatPromptTemplate.from_messages([
    ("system",generic_template),
    ("user","{text}")])
    parser=StrOutputParser()

    
    chain=prompt|model|parser
    response=chain.invoke(user_text)
    return response
