from pytube import YouTube

def download_video(url, output_path='./downloads'):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution='360p').first()
        stream.download(output_path=output_path)
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
