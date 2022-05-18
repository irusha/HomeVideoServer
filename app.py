from asyncio.windows_events import NULL
import numbers
from posixpath import split
from turtle import width
from typing import List
from flask import Flask, render_template
import os
from ffmpy import FFmpeg
from pathlib import Path
import random


thumb_folder = os.getcwd() + "\\static\\Videos\\thumbnails"
if os.path.exists(thumb_folder) == False:
    os.mkdir(thumb_folder)

app = Flask(__name__)
def get_files():
    path = os.getcwd() + "\static\Videos"
    filess = os.listdir(path)
    return filess

files = get_files()


def get_videos():
    final_file_list = []
    for file in files:
        file_split = file.split('.')
        if file_split[len(file_split) - 1] == "mp4":
            final_file_list.append(file)
    return final_file_list

def get_file_name(file):
    return Path(file).stem

get_video_name = {}

def get_thumbnails():
    filess = os.listdir(thumb_folder)
    final_file_list = []
    for file in filess:
        file_split = file.split('.')
        if file_split[len(file_split) - 1] == "png":
            final_file_list.append(file)
    return final_file_list

for thumbName in get_thumbnails():
    get_video_name[thumbName] = get_file_name(thumbName)


def cleanup_thumbs():
    for thumbnail in get_thumbnails():
        print(thumbnail)
            
    
def generate_thumbs(videos):
    path = os.getcwd() + "\\static\\Videos\\"
    for video in videos:
        p = Path(video)
        thumbnail_name = path + 'thumbnails\\' + str(p.with_suffix('.png'))
        if os.path.exists(thumbnail_name) == False:
            videoN = path + video
            print(thumbnail_name)
            ff = FFmpeg(inputs={videoN: None}, outputs={thumbnail_name: ['-ss', '00:00:05', '-vframes', '1']})
            ff.run()


generate_thumbs(get_videos())


@app.route("/")
@app.route("/home")
def hello_world():
    #array_videos = get_videos()
    #video_pairs = [array_videos[x:x+2] for x in range(0, len(array_videos), 2)]
    array_thumbnails = get_thumbnails()
    thumbs_pairs = [array_thumbnails[x:x+3] for x in range(0, len(array_thumbnails), 3)]
    return render_template('index.html', file_pairs = thumbs_pairs, video_names = get_video_name)

@app.route("/videos/<video_name>")
def video_display(video_name):
    array_videos = get_videos()
    array_thumbnails = get_thumbnails()
    thumbs_mini = []
    if len(array_thumbnails) <= 3:
        thumbs_mini = array_thumbnails
    else:
        c = 0
        randoms = []
        while c<3:
            n = random.randint(0, len(array_thumbnails) - 1)
            randoms.append(n)
            c += 1

        dig1 = randoms[0]
        dig2 = randoms[1]
        dig3 = randoms[2]

        while True:
            current_video_index = array_videos.index(video_name + ".mp4")

            if dig1 == dig2:
                randoms[1] = random.randint(0, len(array_thumbnails) - 1)
            elif dig2 == dig3:
                randoms[1] = random.randint(0, len(array_thumbnails) - 1)
            elif dig1 == dig3:
                randoms[2] = random.randint(0, len(array_thumbnails) - 1)
            elif dig1 == current_video_index:
                randoms[1] = random.randint(0, len(array_thumbnails) - 1)
            elif dig2 == current_video_index:
                randoms[1] = random.randint(0, len(array_thumbnails) - 1)
            elif dig1 == current_video_index:
                randoms[2] = random.randint(0, len(array_thumbnails) - 1)
            else:
                break

        for number in randoms:
            thumbs_mini.append(array_thumbnails[number])

    return render_template('video_display.html', video_name = video_name, video_names = get_video_name, video_thumbs = thumbs_mini)
