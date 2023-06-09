import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the YouTube Data API
API_KEY = 'AIzaSyBIPX1w8_nZA-TIj6s1cFhwuOkTVADW0Bo'
YOUTUBE_CHANNEL_ID = 'Vandipranthan'
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to get the subscriber count
def get_subscriber_count():
    try:
        response = youtube.channels().list(
            part='statistics',
            id=YOUTUBE_CHANNEL_ID
        ).execute()

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
subscriber_count = get_subscriber_count()

if subscriber_count is not None:
    st.write(f"Subscriber count: {subscriber_count}")
