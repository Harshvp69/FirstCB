---

**FirstCB - LangChain Chatbot with OpenAI & Streamlit**  

FirstCB is an AI-powered chatbot built using LangChain, OpenAI API, and Streamlit.  
It provides intelligent responses based on user queries and can be extended with additional functionalities.  

## Features  
- Uses OpenAI GPT models (gpt-3.5-turbo, gpt-4)  
- Built with LangChain for efficient AI interactions  
- Streamlit UI for a clean and interactive chat interface  
- Chat History Logging for debugging and improvements  
- Configurable Model Selection from the sidebar  
- "Clear Chat" Button to reset conversations  
- Modular Code Structure (utils/ for reusable functions)  

## Project Structure  
FirstCB/  
│── .gitignore  
│── README.md  
│── requirements.txt  
│── app.py  (Main Streamlit UI)  
│── config.py  (Stores OpenAI API Key securely)  
│── utils/  
│   ├── chat_handler.py  (Handles OpenAI API interaction)  
│   ├── log_handler.py  (Logs chat history)  
│   ├── file_handler.py  (Handles file uploads - optional)  
│   ├── __init__.py  (Makes utils a package - optional)  
│── logs/  
│   ├── chat_logs.txt  (Stores chat logs)  
│── venv/  (optional)  

## Installation & Setup  

1. **Clone the Repository**  
git clone https://github.com/Harshvp69/FirstCB.git  
cd FirstCB  

2. **Create and Activate Virtual Environment**  

On Windows:  
python -m venv venv  
venv\Scripts\activate  

On macOS/Linux:  
python3 -m venv venv  
source venv/bin/activate  

3. **Install Dependencies**  
pip install -r requirements.txt  

4. **Set Up API Key**  
- Create a `.env` file in the root directory.  
- Add your OpenAI API Key:  
OPENAI_API_KEY=your-api-key-here  

## Running the Chatbot  
After installation, start the chatbot with:  
streamlit run app.py  

The app will open in your browser at:  
http://localhost:8501  

## Usage  
- Select a Model (gpt-3.5-turbo or gpt-4) from the sidebar.  
- Type your message in the input box and get an AI-generated response.  
- Click "Clear Chat" to reset the conversation.  
- All chats are logged in `logs/chat_logs.txt`.  

## Future Improvements  
- Memory-based Responses (using a vector database like FAISS)  
- User Authentication System  
- Deploy on Streamlit Cloud or AWS  
- Support for File Uploads & AI Document Analysis  
- Multi-language Support  

## Contributing  
Contributions are welcome! If you’d like to improve this chatbot:  
1. Fork the repository  
2. Create a new branch (`feature-new-functionality`)  
3. Make changes and test  
4. Submit a Pull Request (PR)  

## License  
This project is licensed under the MIT License.  

## Contact  
Author: Harshvardhan P  
GitHub: [Harshvp69](https://github.com/Harshvp69)  

---

