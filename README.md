# HomeHub

### Home Video server

## About
HomeHub - Home video server is made to display your videos at a style. This program can order your files and display them like a video hosting site. It can also recommend you videos from your video folder.

Ths Program is written with python for backend and as a server (Uses Flask library), CSS, HTML, Js for the front end. This program is optimzed for both desktops and mobiles with a separate mobile view. This is an open source software. So anybody can modify and use this software without my consent. The code is not very complex. I think anyone can easily modify this code.


## How to use this software?
First you have to install flask library and ffmpy library from pip. For that use,

"pip install flask"

"pip install ffmpy"

In here the ffmpy library is used to get the thumbnails of the images. The 'ffmpeg.exe' inside the main folder is compulsory for this program to run.

After finish installing the above libraries, open a command window inside the the folder which contains 'app.py' and then enter "flask run" command (or simply run "runserver.bat" to start the server). You will now see the ip address to access your server.


## Important things to know

You have to copy all of your videos to be displayed into "/static/Videos" folder. Otherwise we won't be able to find them.
Due to a limitation of this program, you shouldn't make another "Videos" folder inside the "Videos" folder. This program can only read "mp4" files yet. Fixes incoming
This program never connects to the internet (Refer the code). So we can guarantee a 100% privacy protection.

## Credits


<div style="margin: 20px"><li class="list">
   PalletsProject for flask <a href="https://flask.palletsprojects.com/en" style="text-decoration: none;">Link to flask</a>
</li>
</div>
<div style="margin: 20px"><li class="list">
Google for the icons    
</li>
</div>
<div style="margin: 20px"><li class="list">
   ffmpy for the image converting library <a href="https://ffmpy.readthedocs.io/en/latest/" style="text-decoration: none;">Link</a>
</li>
</div>

<div style="margin: 20px"><li class="list">
   IconScout/Twitter Emoji for the favicon
</li>
</div>
</br>

<h3 style="font-family: Arial, Helvetica, sans-serif; orientation: center; color: rgb(250, 252, 253); margin-left: 20px; text-decoration: none;">Developer
</h3>

<div style="margin: 20px"><p class="paragraph">
    Irusha Sansuka (Amateur programmer)
</p></div>
<a href="https://www.github.com/irusha/HomeVideoServer" class="link">Project Page</a>

<a href="https://www.github.com/irusha" class="link">My github Page</a>

<div style="margin: 20px"><p class="paragraph">
    Email: irushaathukorala@gmail.com
</p>
  
 </div>
  
  # Screenshots
  
  ## Desktop mode
  
  ![image](https://user-images.githubusercontent.com/78542929/169695061-6fcd26a3-d494-48bd-95c9-bf112134797e.png)
  
  Main page
  
  
  ![image](https://user-images.githubusercontent.com/78542929/169695104-30c35db2-f311-47ae-b5bd-4e3e3112d8f0.png)
Video display page
  
  
  ## Mobile View
  
  ![image](https://user-images.githubusercontent.com/78542929/169695200-6085d3cf-9b9c-43db-bc9b-fdbf69510d3e.png)

Main page


![image](https://user-images.githubusercontent.com/78542929/169695274-293af2fd-7a9f-4b71-a299-c7ec26ba19e3.png)

Folder View page


![image](https://user-images.githubusercontent.com/78542929/169695495-197f4fac-aaec-463b-8774-b8e0d235c132.png)
Video display

![image](https://user-images.githubusercontent.com/78542929/169695600-ea8afc68-08d5-4440-884d-4c6b961e0242.png)

Sidebar
