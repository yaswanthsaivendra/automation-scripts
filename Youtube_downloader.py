from pytube import YouTube
from pytube import Playlist

print("imports done")

url = input("Enter the url of the video: ")
print("Fetching video info....")
ytd = YouTube(url)

#print(ytd)
you = ytd.streams.filter(progressive=True).all()
for i in range(len(you)):
    print(str(i)+". "+ str(you[i]))

my_quality = int(input("Enter the quality of video you want to download: "))
print("Downloading video...")
destination = 'E:'
ytd.streams[my_quality].download(destination)
print(str(ytd.streams[my_quality].download()) + " downloaded successfully!!!")

