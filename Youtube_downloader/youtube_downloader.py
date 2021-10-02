from pytube import YouTube

url = input("Enter the url of the video: ")
print("Fetching video info....")
try:
    yt = YouTube(url)

    print("Video Title: ", yt.title)

    you = yt.streams.filter(progressive=True)
    for i in range(len(you)):
        print(str(i)+". " + str(you[i]))
except :
    print(f"Error while fetching the url : {url} ")
else:
    my_quality = input("Enter the quality of video you want to download(Ex: 720p): ")
    print("Downloading video...")

    stream = yt.streams.get_by_resolution(my_quality)
    stream.download()
    print("Successfully downloaded.")

