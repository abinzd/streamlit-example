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
            st.info("Fetching video information... Please wait.")
            
            # Create a YouTube object
            yt = YouTube(video_url)

            # Get video details
            video_title = yt.title
            video_thumbnail = yt.thumbnail_url
            video_author = yt.author
            video_duration = yt.length

            st.subheader("Video Details")
            st.write("Title:", video_title)
            st.write("Author:", video_author)
            st.write("Duration:", video_duration, "seconds")
            st.image(video_thumbnail, use_column_width=True)

            # Provide download link and button
            st.subheader("Download")
            download_link = f"[Download {video_title}](https://www.youtube.com/watch?v={yt.video_id})"
            st.markdown(download_link, unsafe_allow_html=True)
            st.write("")
            st.button("Click to Download", key='download_button', on_click=lambda: download_video(video_url))
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a valid YouTube video URL.")

# Function to initiate download
def download_video(video_url):
    try:
        st.info("Downloading video... Please wait.")
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        st.success("Video downloaded successfully!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
