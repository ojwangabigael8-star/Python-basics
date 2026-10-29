import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'ffmpeg_location': r'C:\'ffmpeg\bin',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
  ydl.download(['https://youtu.be/rn9-UNer6MQ?si=cmZ-HpnpWW3w5dup'])


  #ffmpeg
  # justpaste.it/iq3it


