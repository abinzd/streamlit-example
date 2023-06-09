import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the YouTube Data API
API_KEY = 'AIzaSyBIPX1w8_nZA-TIj6s1cFhwuOkTVADW0Bo'
YOUTUBE_CHANNEL_ID = 'tseries'
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to get the subscriber count
def get_subscriber_count():
    try:
        response = youtube.channels().list(
            part='statistics',
            id=YOUTUBE_CHANNEL_ID
        ).execute()

        items = response['items']
        subscriber_count = int(items[0]['statistics']['subscriberCount'])
        return subscriber_count
    except HttpError as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit app
st.title('Real-time YouTube Subscribers')
subscriber_count = get_subscriber_count()

if subscriber_count is not None:
    st.write(f"Subscriber count: {subscriber_count}")

# Run the Streamlit app
if __name__ == '__main__':
    st.run_app()
