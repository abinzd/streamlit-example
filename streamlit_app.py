import random
import streamlit as st
from pytube import YouTube, Playlist, Channel
import os

# Function for some random animations
def random_celeb():
    return random.choice([st.balloons()])

# Function to download YouTube single videos
# Function to download YouTube single videos
def video(url):
    video_caller = YouTube(url)
    st.info(video_caller.title, icon="ℹ️")

    # Get available video streams
    streams = video_caller.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

    # Create a dictionary to store resolution and corresponding streams
    resolution_dict = {}
    for stream in streams:
        resolution = f"{stream.resolution} ({stream.mime_type.split('/')[1]})"
        resolution_dict[resolution] = stream

    # Get the available resolutions
    resolutions = list(resolution_dict.keys())

    # Display resolution options
    resolution = st.selectbox("Select Video Resolution", resolutions)

    # Find the selected stream based on the resolution string
    selected_stream = resolution_dict.get(resolution)

    if selected_stream is not None:
        # Display audio options
        audio_streams = video_caller.streams.filter(only_audio=True).order_by('abr').desc()
        audio_formats = [stream.abr for stream in audio_streams]
        audio_format = st.selectbox("Select Audio Format", audio_formats)

        # Find the selected audio stream based on the format string
        selected_audio_stream = audio_streams[audio_formats.index(audio_format)]

        # Download video and audio
        selected_stream.download(filename_prefix='video_')
        selected_audio_stream.download(filename_prefix='audio_')
        st.success('Done!')

        # Merge video and audio files
        video_file = f'video_{selected_stream.default_filename}'
        audio_file = f'audio_{selected_audio_stream.default_filename}'
        output_file = f'merged_{selected_stream.default_filename}'
        os.system(f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac "{output_file}"')

        # Provide download link for the merged file
        with open(output_file, 'rb') as file:
            st.download_button('Download Video', file, file_name=output_file)
        
        # Delete temporary files
        os.remove(video_file)
        os.remove(audio_file)
        os.remove(output_file)
    else:
        st.error('Oops! Stream is not available!')


# Function for downloading YouTube playlist
def playlist(url):
    playlist_obj = Playlist(url)
    st.info('Number of videos in playlist: %s' % len(playlist_obj.video_urls), icon="ℹ️")
    for video in playlist_obj.videos:
        x = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if x is not None:
            x.download()
            st.success('Done!')
            with open(selected_stream.default_filename, 'rb') as file:
                st.download_button('Download Video', file, file_name=x.default_filename + '.mp4')

# Function for downloading YouTube channel
def channel(url):
    channel_videos = Channel(url)
    st.info(f'Downloading videos by: {channel_videos.channel_name}', icon="ℹ️")
    for video in channel_videos.videos:
        z = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if z is not None:
            z.download()
            st.success('Done!')
            with open(selected_stream.default_filename, 'rb') as file:
                st.download_button('Download Channel', file, file_name=z.default_filename + '.mp4')

# Integration of all above-defined functions
st.title("YouTube Downloader")
url = st.text_input(label="Paste your YouTube URL")
if st.button("Download"):
    if url:
        try:
            with st.spinner("Loading..."):
                if 'playlist' in url:
                    playlist(url)
                elif 'channel' in url:
                    channel(url)
                else:
                    video(url)
            random_celeb()
        except Exception as e:
            st.error(e)
