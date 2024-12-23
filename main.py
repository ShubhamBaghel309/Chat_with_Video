import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
import groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_video_id(url):
    """Extract YouTube video ID from URL."""
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_transcript(video_id):
    """Get transcript from YouTube video."""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([t["text"] for t in transcript_list])
    except TranscriptsDisabled:
        return None

def generate_summary(transcript, summary_type="short"):
    """Generate summary using Groq API."""
    if summary_type == "short":
        prompt = f"Please provide a concise summary (2-3 sentences) of the following transcript:\n\n{transcript}"
    elif summary_type == "detailed":
        prompt = f"Please provide a detailed summary (4-5 paragraphs) of the following transcript:\n\n{transcript}"
    else:  # bullet points
        prompt = f"Please provide a bullet-point summary of the key points from the following transcript:\n\n{transcript}"

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that specializes in summarizing video content."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0.5,
    )
    
    return chat_completion.choices[0].message.content

def chat_with_bot(transcript, question):
    """Chat with the bot about the video content."""
    prompt = f"""Given the following video transcript:

{transcript}

Please answer this question: {question}"""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that answers questions about video content based on its transcript."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0.7,
    )
    
    return chat_completion.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="chat with video", layout="wide")

st.title("🎥 YouTube Video Summarizer")
st.write("Get summaries and chat about any YouTube video!")

# Video URL input
video_url = st.text_input("Enter YouTube Video URL:")

if video_url:
    video_id = extract_video_id(video_url)
    
    if video_id:
        # Display video
        st.video(video_url)
        
        # Get transcript
        transcript = get_transcript(video_id)
        
        if transcript:
            # Create tabs for different functionalities
            tab1, tab2, tab3 = st.tabs(["📝 Summaries", "💬 Chat", "📜 Full Transcript"])
            
            with tab1:
                st.subheader("Video Summaries")
                summary_type = st.radio(
                    "Choose summary type:",
                    ["Short", "Detailed", "Bullet Points"],
                    horizontal=True
                )
                
                if st.button("Generate Summary"):
                    with st.spinner("Generating summary..."):
                        summary = generate_summary(transcript, summary_type.lower())
                        st.markdown(summary)
                        
                        # Download button for summary
                        st.download_button(
                            "Download Summary",
                            summary,
                            file_name="video_summary.txt",
                            mime="text/plain"
                        )
            
            with tab2:
                st.subheader("Chat about the Video")
                user_question = st.text_input("Ask a question about the video:")
                
                if user_question:
                    with st.spinner("Thinking..."):
                        response = chat_with_bot(transcript, user_question)
                        st.markdown(response)
            
            with tab3:
                st.subheader("Full Transcript")
                st.text_area("Video Transcript", transcript, height=300)
        else:
            st.error("Sorry, couldn't retrieve the transcript for this video. It might be disabled or unavailable.")
    else:
        st.error("Invalid YouTube URL. Please check the URL and try again.")
