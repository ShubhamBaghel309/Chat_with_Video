# YouTube Video Summarizer

This project is a **Streamlit-based web application** that provides concise and detailed summaries, bullet-point highlights, and Q&A capabilities for YouTube videos. The app leverages the YouTube Transcript API for retrieving video transcripts and the Groq API for generating summaries and answering user questions about the video content.

---

## Features

1. **Video Summaries**
   - Generate **short**, **detailed**, or **bullet-point** summaries of a YouTube video.
   - Download the generated summaries as text files.

2. **Interactive Q&A**
   - Chat with the bot to ask specific questions about the content of the video.

3. **Full Transcript Display**
   - View the entire transcript of the YouTube video in a text area.

4. **Responsive UI**
   - Interactive and intuitive Streamlit interface.
   - Embeds the YouTube video for better context.

---

## Installation

### Prerequisites
- Python 3.8 or later
- An API key for the **Groq API**
- A `.env` file containing your Groq API key as follows:
  ```
  GROQ_API_KEY=your_api_key_here
  ```

### Clone the Repository
```bash
https://github.com/your-repo/youtube-video-summarizer.git
cd youtube-video-summarizer
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Run the Application
```bash
streamlit run app.py
```

### How to Use
1. Enter the URL of the YouTube video in the input field.
2. Wait for the transcript to load.
3. Navigate through the tabs:
   - **Summaries**: Select a summary type (short, detailed, or bullet points) and generate a summary.
   - **Chat**: Ask questions about the video content and receive detailed answers.
   - **Full Transcript**: View the entire transcript of the video.

4. Download summaries or interact with the transcript as needed.

---

## Project Structure
```plaintext
.
├── app.py               # Main application file
├── requirements.txt     # List of Python dependencies
├── .env                 # Environment variables file (GROQ_API_KEY)
└── README.md            # Project documentation
```

---

## APIs Used

1. **YouTube Transcript API**
   - Retrieves transcripts of YouTube videos.
   - [Documentation](https://pypi.org/project/youtube-transcript-api/)

2. **Groq API**
   - Used for generating summaries and answering questions based on video transcripts.
   - Requires an API key.

---

## Future Enhancements
- Add multilingual support for non-English video transcripts.
- Integrate more advanced AI models for richer context understanding.
- Enable support for videos without transcripts using speech-to-text models.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments
- **Streamlit**: For providing an excellent framework for building web applications.
- **YouTube Transcript API**: For enabling easy access to video transcripts.
- **Groq API**: For powerful summarization and Q&A capabilities.
