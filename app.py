from asyncio.windows_events import NULL
from posixpath import split
from flask import Flask, render_template
import os
from ffmpy import FFmpeg
from pathlib import Path
from random import sample

videos_folder = "\\static\\Videos\\"
items_per_page = 5

app = Flask(__name__)
def get_files(directory):
    path = os.getcwd() + directory
    filess = os.listdir(path)
    return filess


def get_files_with_extension(files, extension):
    final_file_list = []
    for file in files:
        file_split = file.split('.')
        if file_split[len(file_split) - 1] == extension:
            final_file_list.append(file)
    return final_file_list


def get_folders(current_folder):
    path = os.getcwd() + "\\static\\" + current_folder
    folder_list = []
    for folder in next(os.walk(path, '.'))[1]:
        if folder != 'thumbnails':
            folder_list.append(folder)

    return folder_list


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
    filesList = get_files(folder_path)
    videos = get_files_with_extension(filesList, 'mp4')
    path = os.getcwd() + folder_path
    for video in videos:
        p = Path(video)
        thumbnail_name = path + 'thumbnails\\' + str(p.with_suffix('.png'))
        if os.path.exists(thumbnail_name) == False:
            videoN = path + video
            print(thumbnail_name)
            ff = FFmpeg(inputs={videoN: None}, outputs={thumbnail_name: ['-ss', '00:00:20', '-vframes', '1']})
            ff.run()


#First we have to clean up thumbnails of the old videos and generate thumbnails for new videos
for folder in get_folders('Videos'):
    cleanup_thumbs(videos_folder + folder + "\\")
    generate_thumbs(videos_folder + folder + "\\")
    array_thumbnails = get_thumbnails(videos_folder + folder + "\\")
    for thumbName in array_thumbnails:
        get_video_name[thumbName] = get_file_name(thumbName)


cleanup_thumbs(videos_folder)
generate_thumbs(videos_folder)
for thumbName in get_thumbnails(videos_folder):
    get_video_name[thumbName] = get_file_name(thumbName)


#Search for every file in the directory
list_of_every_file = []
for root, dirs, files in os.walk(os.getcwd() + "\\" + videos_folder):
	for file in files:
        #append the file name to the list
		list_of_every_file.append(os.path.join(root,file))


#clean up files list to only contain .png fies
every_thumbnail_paths = get_files_with_extension(list_of_every_file, 'png')


#Get a list that contains only the file names
every_thumbnail_names = []
for curr_path in every_thumbnail_paths:
    every_thumbnail_names.append(str(get_file_name(curr_path)))


#Get the path of the video
every_video_path = []
for curr_path in every_thumbnail_paths:
    splitPath = curr_path.split("\\")
    if (splitPath[len(splitPath)-3] == 'Videos'):
        every_video_path.append("Videos/")
    else:
        every_video_path.append("Videos/" + splitPath[len(splitPath)-3] + "/")


#Add the file name and relevent path to a dictionary
file_links_dictionary = {}
for curr_ind in range(0, len(every_thumbnail_names)):
    file_links_dictionary[every_thumbnail_names[curr_ind]] = every_video_path[curr_ind]


@app.route("/")
@app.route("/home")
def hello_world():
    cleanup_thumbs(videos_folder)
    generate_thumbs(videos_folder)
    array_thumbnails = get_thumbnails(videos_folder)
    for thumbName in get_thumbnails("\\static\\Videos"):
        get_video_name[thumbName] = get_file_name(thumbName)
    return render_template('index.html', files = array_thumbnails, video_names = get_video_name, folders = get_folders('Videos'))


@app.route("/videos/<video_name>")
def video_display(video_name):
    if video_name in file_links_dictionary:
        thumbs_mini = sample(every_thumbnail_names, 4)
        return render_template('video_display.html', video_name = video_name, video_names = get_video_name, video_thumbs = thumbs_mini, file_links = file_links_dictionary, folders = get_folders('Videos'))
    else:
        return render_template('404_error.html')

@app.route("/folders/<folder_name>")
def folder_display(folder_name):
    try:
        cleanup_thumbs(videos_folder + folder_name + "\\")
        generate_thumbs(videos_folder + folder_name + "\\")
        array_thumbnails = get_thumbnails(videos_folder + folder_name + "\\")
        for thumbName in array_thumbnails:
            get_video_name[thumbName] = get_file_name(thumbName)
        
        thumbs_pairs = [array_thumbnails[x:x+25] for x in range(0, len(array_thumbnails), 25)]
        return render_template('folder_view.html', name = folder_name, files = array_thumbnails, video_names = get_video_name, folders = get_folders('Videos'))

    except:
        return render_template('404_error.html')


@app.route("/m")
def m_index():
    cleanup_thumbs(videos_folder)
    generate_thumbs(videos_folder)
    array_thumbnails = get_thumbnails(videos_folder)
    thumb_groups = [array_thumbnails[x:x+items_per_page] for x in range(0, len(array_thumbnails), items_per_page)]
    for thumbName in get_thumbnails("\\static\\Videos"):
        get_video_name[thumbName] = get_file_name(thumbName)
    return render_template('index_m.html', files = thumb_groups[0], video_names = get_video_name, folders = get_folders('Videos'), pages =len(thumb_groups) - 1 )
    

@app.route("/m/folders/<folder_name>")
def folder_display_m(folder_name):
    try:
        cleanup_thumbs(videos_folder + folder_name + "\\")
        generate_thumbs(videos_folder + folder_name + "\\")
        array_thumbnails = get_thumbnails(videos_folder + folder_name + "\\")
        thumb_groups = [array_thumbnails[x:x+items_per_page] for x in range(0, len(array_thumbnails), items_per_page)]
        for thumbName in array_thumbnails:
            get_video_name[thumbName] = get_file_name(thumbName)
        return render_template('folder_view_m.html', name = folder_name, files = thumb_groups[0], video_names = get_video_name, folders = get_folders('Videos'), pages =len(thumb_groups) - 1)
    except:
        return render_template('404_error.html')

@app.route("/m/videos/<video_name>")
def video_display_m(video_name):
    if video_name in file_links_dictionary:
        thumbs_mini = sample(every_thumbnail_names, 4)
        return render_template('video_display_m.html', video_name = video_name, video_names = get_video_name, video_thumbs = thumbs_mini, file_links = file_links_dictionary, folders = get_folders('Videos'))
    else:
        return render_template('404_error.html')


@app.route("/m/page<number>")
def pages_home(number):
    array_thumbnails = get_thumbnails(videos_folder)
    thumb_groups = [array_thumbnails[x:x+items_per_page] for x in range(0, len(array_thumbnails), items_per_page)]
    try:
        if int(number) >= len(thumb_groups):
            return render_template('404_error.html')
        else:    
            cleanup_thumbs(videos_folder)
            generate_thumbs(videos_folder)
            for thumbName in get_thumbnails("\\static\\Videos"):
                get_video_name[thumbName] = get_file_name(thumbName)
            return render_template('index_m.html', files = thumb_groups[int(number) - 1], video_names = get_video_name, folders = get_folders('Videos'), pages =len(thumb_groups) - 1)
    except:
        return render_template('404_error.html')


@app.route("/m/folders/<folder_name>/page<number>")
def pages_folders(folder_name, number):
    try:
        cleanup_thumbs(videos_folder + folder_name + "\\")
        generate_thumbs(videos_folder + folder_name + "\\")
        array_thumbnails = get_thumbnails(videos_folder + folder_name + "\\")
        thumb_groups = [array_thumbnails[x:x+items_per_page] for x in range(0, len(array_thumbnails), items_per_page)]
        for thumbName in array_thumbnails:
            get_video_name[thumbName] = get_file_name(thumbName)
        return render_template('folder_view_m.html', name = folder_name, files = thumb_groups[int(number) - 1], video_names = get_video_name, folders = get_folders('Videos'), pages =len(thumb_groups) - 1 )
    except:
        return render_template('404_error.html')
