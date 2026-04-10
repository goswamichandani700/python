#findout python pakcage to download youtube video
import yt_dlp

url = "https://youtu.be/LUx8wlA_dk8?si=N6zJT_No12-GnUT2"

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed!")