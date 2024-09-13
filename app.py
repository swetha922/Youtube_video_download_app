import streamlit as st
from pytube import YouTube
from yt_dlp import YoutubeDL
import os

# Streamlit app title
st.set_page_config(page_title='YouTube Video Download')
st.title('YouTube Video Downloader')

# Input for YouTube link
video_link = st.text_input('Enter the YouTube video URL:')
st.write('Ready to download!')

# Ensure the 'downloads' folder exists for saving the videos
if not os.path.exists('downloads'):
    os.makedirs('downloads')

# Button to download the video
if st.button('Download Video'):
    if video_link:
        try:
            yt = YouTube(video_link)
            st.subheader(f"Video Title: {yt.title}")
            
            # yt-dlp options to save the video in 'downloads' folder
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'downloads/%(title)s.%(ext)s'  # Save in 'downloads' folder
            }

            with YoutubeDL(ydl_opts) as ydl:
                st.write("Downloading...")
                ydl.download([video_link])
                st.success('Download completed!')

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please enter a valid YouTube URL.")
