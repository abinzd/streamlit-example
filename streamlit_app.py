import streamlit as st
from pytube import YouTube

# Page setup
st.title("YouTube Downloader")

# Get YouTube video URL from user
video_url = st.text_input("Enter YouTube video URL:", "")

# Process the video URL
if st.button("Download"):
    if video_url:
        try:
            st.info("Downloading video... Please wait.")
            
            # Create a YouTube object
            yt = YouTube(video_url)

            # Get the highest resolution stream
            stream = yt.streams.get_highest_resolution()

            # Download the video
            stream.download()

            st.success("Video downloaded successfully!")
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a valid YouTube video URL.")
