from pytube import YouTube

url = "https://www.youtube.com/watch?v=siCyNyda0gA"
my_video = YouTube(url)

print("**************************Video title******************")
print(my_video.title)

print("**************************Thumbnail******************")
print(my_video.thumbnail_url)

print("**************************Download video******************")
my_video = my_video.streams.get_highest_resolution()

my_video.download()