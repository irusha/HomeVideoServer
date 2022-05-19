from asyncio.windows_events import NULL
from posixpath import split
from flask import Flask, render_template
import os
from ffmpy import FFmpeg
from pathlib import Path
import random




app = Flask(__name__)
def get_files(directory):
    path = os.getcwd() + directory
    filess = os.listdir(path)
    return filess


def get_videos(directory):
    final_file_list = []
    files = get_files(directory)
    for file in files:
        file_split = file.split('.')
        if file_split[len(file_split) - 1] == "mp4":
            final_file_list.append(file)
    return final_file_list

def get_folders(current_folder):
    path = os.getcwd() + "\\static\\" + current_folder
    folder_list = []
    for folder in next(os.walk(path, '.'))[1]:
        if folder != 'thumbnails':
            folder_list.append(folder)

    return folder_list

print(get_folders("Videos")[0])


def get_file_name(file):
    return Path(file).stem

get_video_name = {}

#folder_path is the folder that contains the videos
#By default, thumbnails folder automatically created in static\Videos
#Returns the thumbnails of the videos inside the folder that is given to folder_path argument
def get_thumbnails(folder_path):
    thumb_folder = os.getcwd() + folder_path + "\\thumbnails"
    if os.path.exists(thumb_folder) == False:
        os.mkdir(thumb_folder)
    filess = os.listdir(thumb_folder)
    final_file_list = []
    for file in filess:
        file_split = file.split('.')
        if file_split[len(file_split) - 1] == "png":
            final_file_list.append(file)
    return final_file_list


#folder_path is the folder that contains the videos
#Function cleans up unnecessary thumbnails
def cleanup_thumbs(folder_path):
    for thumbnail in get_thumbnails(folder_path):
        path = os.getcwd() + folder_path
        video_name = path + get_file_name(thumbnail) + ".mp4"
        if os.path.exists(video_name) == False:
            os.remove(path + "thumbnails\\" + thumbnail)
    
#Function generates thumbnails for the videos inside the given folder_path
#Thumbnails are stored in the folder "thumbnails"
def generate_thumbs(folder_path):
    videos = get_videos(folder_path)
    path = os.getcwd() + folder_path
    for video in videos:
        p = Path(video)
        thumbnail_name = path + 'thumbnails\\' + str(p.with_suffix('.png'))
        if os.path.exists(thumbnail_name) == False:
            videoN = path + video
            print(thumbnail_name)
            ff = FFmpeg(inputs={videoN: None}, outputs={thumbnail_name: ['-ss', '00:00:20', '-vframes', '1']})
            ff.run()


@app.route("/")
@app.route("/home")
def hello_world():
    cleanup_thumbs("\\static\\Videos\\")
    generate_thumbs("\\static\\Videos\\")
    array_thumbnails = get_thumbnails("\\static\\Videos\\")
    for thumbName in get_thumbnails("\\static\\Videos"):
        get_video_name[thumbName] = get_file_name(thumbName)
    thumbs_pairs = [array_thumbnails[x:x+3] for x in range(0, len(array_thumbnails), 3)]
    return render_template('index.html', file_pairs = thumbs_pairs, video_names = get_video_name, folders = get_folders('Videos'))

@app.route("/videos/<video_name>")
def video_display(video_name):
    array_videos = get_videos("\static\Videos")
    array_thumbnails = get_thumbnails("\\static\\Videos\\")
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

        k = 0
        while k < 15:
            current_video_index = array_videos.index(video_name + ".mp4")
            print(current_video_index)

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
            k += 1

        for number in randoms:
            thumbs_mini.append(array_thumbnails[number])

    return render_template('video_display.html', video_name = video_name, video_names = get_video_name, video_thumbs = thumbs_mini)

@app.route("/folders/<folder_name>")
def folder_display(folder_name):
    cleanup_thumbs("\\static\\Videos\\" + folder_name + "\\")
    generate_thumbs("\\static\\Videos\\" + folder_name + "\\")
    array_thumbnails = get_thumbnails("\\static\\Videos\\" + folder_name + "\\")
    for thumbName in array_thumbnails:
        get_video_name[thumbName] = get_file_name(thumbName)
    thumbs_pairs = [array_thumbnails[x:x+3] for x in range(0, len(array_thumbnails), 3)]
    return render_template('folder_view.html', name = folder_name, file_pairs = thumbs_pairs, video_names = get_video_name, folders = get_folders('Videos'))
