from pytube import YouTube

f_r = open("input/playlist.txt", "rt")

for i in f_r.readlines():
    yt= YouTube(i)
    yt.streams.filter(progressive=True, file_extension="mp4").desc().first().download("output/")
f_r.close()
