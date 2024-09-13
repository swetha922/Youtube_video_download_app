# YouTube Video Downloader

# Overview

This is a simple web application built with Streamlit that allows users to download YouTube videos. The app leverages the pytube library to fetch video details and yt-dlp for downloading the video content. All downloaded videos are saved in a local downloads folder.

# Features

Input Field: Enter the URL of the YouTube video you want to download.

Download Button: Click to start downloading the video.

Video Title Display: Shows the title of the video being downloaded.

Error Handling: Displays error messages if something goes wrong.

# Requirements
To run this app, you need to have Python installed along with the following packages:

streamlit

pytube

yt-dlp

# How It Works
The app starts by allowing the user to input a YouTube video URL.

Upon clicking the "Download Video" button, it fetches video details and starts downloading the video using yt-dlp.

The video is saved in the downloads folder with the title of the video as the filename.

# Troubleshooting
Invalid URL: Ensure the YouTube URL is correctly entered and try again.

No Downloads Folder: The app will automatically create a downloads folder if it doesn't exist.

Error Messages: If an error occurs, the app will display the error message for debugging purposes.
