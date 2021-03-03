# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from pytube import Playlist

ytd = Playlist('https://www.youtube.com/watch?v=gsT6eKsnT0M&list=PLeLvSt3A0DdmAUlRdqg4jp5MAuh04APIW')

for video in ytd.videos:
    print(video.title)
    print(video.streams.filter(only_audio=True).first())
