from __future__ import print_function
from mimetypes import init
from matplotlib.pyplot import title
from pytube import YouTube

link = input("paste the video link here:")

youtube = YouTube(link)

videos = youtube.streams.all()
vid = list(enumerate(videos))

for i in vid:
    print(i)

print()
strm  = int(input("enter index:"))
videos[strm].download()
print("successfully downladed!")

# for downloading full full playlist copy the code below:

# from pytube import Playlist
# videos = youtube.streams.all()
# playlist_link = input("paste the playlist link here:")
# py = Playlist(playlist_link)

# print(f'Downloading:{py.title}')
# for video in py.videos:
#     videos.stream.first().download()
