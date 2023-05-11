import ssl
import sys
import yt_dlp

ssl._create_default_https_context = ssl._create_unverified_context

def download_age_restricted_video(url):
    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
        'age_limit': 99,
        'merge_output_format': 'mp4',
        'postprocessor_args': [
            '-c:v', 'libx264', '-c:a', 'aac', '-strict', '-2'
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Downloading video: {url}")
            ydl.download([url])
            print(f"Download and conversion complete for: {url}")
        except Exception as e:
            print(f"Error downloading video: {url}")
            print(e)

def main():
    if len(sys.argv) < 2:
        print("Please provide a YouTube URL as an argument.")
        return

    url = sys.argv[1]
    download_age_restricted_video(url)

if __name__ == "__main__":
    main()
