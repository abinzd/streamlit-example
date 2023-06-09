import re
import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the YouTube Data API
API_KEY = 'AIzaSyBIPX1w8_nZA-TIj6s1cFhwuOkTVADW0Bo'
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to extract channel ID from YouTube link
def extract_channel_id(link):
    pattern = r"(?:(?:https?:\/\/)?(?:www\.)?youtube\.com\/(?:c\/|channel\/|user\/))([^\/\?\&\n]{11})"
    match = re.search(pattern, link)
    if match:
        return match.group(1)
    return None


# Function to get the subscriber count
def get_subscriber_count(channel_id):
    try:
        response = youtube.channels().list(
            part='statistics',
            id=channel_id
        ).execute()

        print(response)  # Print the response for debugging purposes

        items = response.get('items', [])
        if len(items) > 0:
            statistics = items[0]['statistics']
            subscriber_count = int(statistics['subscriberCount'])
            return subscriber_count

        st.error('No channel data found in the API response.')
        return None

    except HttpError as e:
        st.error(f"An error occurred: {e}")
        return None


# Streamlit app
st.title('Real-time YouTube Subscribers')

# Accept YouTube link from user
youtube_link = st.text_input('Enter a YouTube channel link:')
channel_id = extract_channel_id(youtube_link)

if channel_id:
    subscriber_count = get_subscriber_count(channel_id)

    if subscriber_count is not None:
        st.write(f"Subscriber count: {subscriber_count}")
else:
    st.warning('Invalid YouTube channel link entered.')

