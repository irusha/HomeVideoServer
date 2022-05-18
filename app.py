from posixpath import split
from turtle import width
from typing import List
from flask import Flask, render_template
import os
from ffmpy import FFmpeg
from pathlib import Path

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

def get_thumbnails():
    
    filess = os.listdir(thumb_folder)
    final_file_list = []
    for file in filess:
        file_split = file.split('.')
        if file_split[len(file_split) - 1] == "png":
            final_file_list.append(file)
    return final_file_list


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
    return render_template('index.html', file_pairs = thumbs_pairs)

@app.route("/paka/")
def ok_fun():
    return "Ranil ponnaya"
