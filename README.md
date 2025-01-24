# Multilingual-Assistant-GenAI

This is a multilingual voice AI assistant that can respond to user input in both voice and text. It is designed to provide a personalized and dynamic conversational experience by retaining chat history and remembering previous conversations.

Features
Voice and Text Responses: The assistant responds to user input both in text and voice.
Multilingual Support: Can understand and reply in multiple languages, based on the user's input language.
Chat History Retention: The assistant retains previous chat history for personalized interactions.
Conversation Memory: Remembers past conversations, providing context to the current interaction.
Interactive Interface: Built using Streamlit for easy deployment and use.
Technologies Used
Streamlit: A framework to build the interactive web interface for the voice AI assistant.
Langchain Expression Language: Used for handling multiple languages and enabling multilingual interactions.
Geema LLM from Groq API: A large language model used for processing and generating responses in different languages.
EC2: Deployed on Amazon EC2 for scalability and cloud hosting.
Installation and Setup
To run this project locally, follow these steps:

1. Clone the repository
bash
Copy
Edit
git clone <repository-url>
cd <repository-folder>
2. Install the dependencies
Install the required packages using pip:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the Streamlit app
Once the dependencies are installed, run the app with the following command:

bash
Copy
Edit
streamlit run app.py
4. Access the app
Open your browser and go to http://localhost:8501 to interact with the AI assistant.

How It Works
User Input: Users can speak or type their queries in any supported language.
Processing: The assistant processes the input using Geema LLM via the Groq API and generates an appropriate response.
Response: The assistant replies both in voice and text, allowing the user to engage through either medium.
Memory: The assistant stores the conversation history and can reference previous interactions for a more personalized experience.