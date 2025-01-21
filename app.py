import streamlit as st
from multilingual.helper import text_to_speeh,voice_input,llm_model_object
from langchain_groq import ChatGroq
import os
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
groq_api_key=os.getenv("GROQ_API_KEY")
session_id=st.text_input("session ID",value="default_session")

if 'store' not in st.session_state:
                st.session_state.store={}

def main():
    st.title('Multilingual Assistant GenAI 🤖')
    button=st.button('Ask me Anything')
    if button:
        with st.spinner("Listening..."):
            text=voice_input()
            st.write(text)#speech to text converted
            
            

            

            model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)
    
            generic_template=("""You are name is Rispah 
            and you are an advanced multilingual AI assistant
         created to assist users seamlessly using 
        various languages, cultures, and contexts.
        You are highly fluent in English, Tamil,
        Spanish, French, German, Chinese, Hindi, 
        Arabic, Japanese, Portuguese, Russian, and other 
        major languages. Your primary goal is to provide accurate, 
        relevant, and contextually appropriate responses while ensuring 
        a user-friendly experience.
        "/n/n"
        
        """)
    
            prompt=ChatPromptTemplate.from_messages([
        ("system",generic_template),
        MessagesPlaceholder("chat_history"),
        ("user","{input}")])


            chain=prompt|model


            


            def get_session_history(session_id:str):

                if session_id not in st.session_state.store:
                    st.session_state.store[session_id]=ChatMessageHistory()
                return st.session_state.store[session_id] 
        
            chain2 = RunnableWithMessageHistory(
                chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history") 


                
                        
       
    
            if text is None:


                response=llm_model_object(text)#text output from model
                text_to_speeh(response)#converts model text reponse to sppech and saves it local
                print(st.session_state.store)

            else: 
                  session_history=get_session_history(session_id)
                  result=chain2.invoke(
                {"input":text},config={"configurable":{"session_id":session_id}})
                  response=result.content
                  text_to_speeh(response)#converts model text reponse to sppech and saves it local
                  print(st.session_state.store)

   


            audio_file=open('speech.mp3','rb')
            audio_byte=audio_file.read()

            st.text_area(label="Response:",value=response,height=350)
            st.audio(audio_byte)
            st.download_button(label='Download Speech',data=audio_byte,file_name="speech.mp3",mime="audio/mp3")

if __name__ == '__main__':
    main()        