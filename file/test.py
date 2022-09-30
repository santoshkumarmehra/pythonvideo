#pytube

from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=NvuQ9Eskl04&ab_channel=RaagBandMusic')
yt.streams.filter(file_extension='mp4')

stream = yt.streams.get_by_itag(22)
stream.download(filename='ytvideo',output_path='/home/codetrade')





