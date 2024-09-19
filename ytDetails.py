import os
import csv
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from pytube import Playlist

# Function to create the 'playlist_details' folder if it doesn't exist
def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Function to extract playlist details and save to CSV
def extract_playlist_details(playlist_url):
    try:
        playlist = Playlist(playlist_url)

        # Create a folder for playlist details
        folder_name = "playlist_details"
        create_folder_if_not_exists(folder_name)

        # Get the current date and time for the CSV file name
        current_time = datetime.now().strftime('%d-%m-%Y-%I-%M-%S-%p')
        csv_filename = os.path.join(folder_name, f"{current_time}.csv")

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Video Title', 'Video URL'])

            for video in playlist.video_urls:
                # Get the video title
                response = requests.get(video)
                soup = BeautifulSoup(response.text, 'html.parser')
                video_title = soup.find('title').text.strip()

                # Write video title and URL to the CSV file
                csv_writer.writerow([video_title, video])

        print(f"Playlist details saved to {csv_filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    playlist_url = input("Enter the YouTube playlist URL: ")
    extract_playlist_details(playlist_url)
