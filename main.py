from pytube import YouTube
import moviepy.editor as mp
import os

banner =r'''

 __     _________     _____                      _                 _           
 \ \   / /__   __|   |  __ \                    | |               | |          
  \ \_/ /   | |______| |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   \   /    | |______| |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    | |     | |      | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
    |_|     |_|      |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_| 
                            created by #BreckzTv

'''
print(banner)
# YouTube video URL
url = input("Geben sie die Url an: ")

# Download YouTube video
yt = YouTube(url)
stream = yt.streams.filter(only_audio=True).first()
output_path = 'downloads'
filename = 'audio'
file_path = os.path.join(output_path, f'{filename}.mp4')

# Ensure the output path exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Download the audio stream
stream.download(output_path=output_path, filename=f'{filename}.mp4')

# Convert video to MP3
clip = mp.AudioFileClip(file_path)
mp3_file_path = os.path.join(output_path, f'{filename}.mp3')
clip.write_audiofile(mp3_file_path)

# Clean up: remove the original .mp4 file if needed
os.remove(file_path)

print(f"Audio successfully downloaded and converted to {mp3_file_path}.")
