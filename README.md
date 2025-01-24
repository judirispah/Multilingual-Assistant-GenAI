# Multilingual Voice AI Assistant

This is a **multilingual voice AI assistant** that can respond to user input in both **voice** and **text**. It is designed to provide a personalized and dynamic conversational experience by retaining chat history and remembering previous conversations.

## Features
- **Voice and Text Responses**: The assistant responds to user input both in text and voice.
- **Multilingual Support**: Can understand and reply in multiple languages, based on the user's input language.
- **Chat History Retention**: The assistant retains previous chat history for personalized interactions.
- **Conversation Memory**: Remembers past conversations, providing context to the current interaction.
- **Interactive Interface**: Built using **Streamlit** for easy deployment and use.
  
## Technologies Used
- **Streamlit**: A framework to build the interactive web interface for the voice AI assistant.
- **Langchain Expression Language**: Used for handling multiple languages and enabling multilingual interactions.
- **Gemma LLM from Groq API**: A large language model used for processing and generating responses in different languages.


## Installation and Setup

To run this project locally, follow these steps:

### 1. Clone the repository
```bash
git clone <repository-url>
cd <repository-folder>

## Installation and Setup

To get started with the Multilingual Voice AI Assistant, follow these steps:

### 2. Install the dependencies
```bash
pip install -r requirements.txt

### 3. run the streamlit app
```bash
streamlit run app.py

## How It Works

1. **User Input**: 
   - Users can speak or type their queries in any supported language.
   
2. **Processing**: 
   - The assistant processes the input using **Geema LLM** via the **Groq API** and generates an appropriate response.
   
3. **Response**: 
   - The assistant replies in both **voice** and **text**, allowing the user to engage through either medium.
   
4. **Memory**: 
   - The assistant stores the conversation history and can reference previous interactions for a more personalized experience.





