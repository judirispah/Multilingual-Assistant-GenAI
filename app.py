import streamlit as st
from multilingual.helper import text_to_speeh,voice_input,llm_model_object
import time

def main():
    st.title('Multilingual Assistant GenAI 🤖')
    button=st.button('Ask me Anything')
    if button:
        with st.spinner("Listening..."):
            text=voice_input()
            st.write(text)#speech to text converted
            response=llm_model_object(text)#text output from model
            text_to_speeh(response)#converts model text reponse to sppech and saves it local


            audio_file=open('speech.mp3','rb')
            audio_byte=audio_file.read()

            st.text_area(label="Response:",value=response,height=350)
            st.audio(audio_byte)
            st.download_button(label='Download Speech',data=audio_byte,file_name="speech.mp3",mime="audio/mp3")

if __name__ == '__main__':
    main()        