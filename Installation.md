The hardware you need is a Raspberry Pi 3 model B, with a Pi Camera (a box is optional), running on Raspbian; and a pendulum which can be made with a 
lead bead of about 1 cm. radius, hanging from a thread (a half a meter long thin thread is suitable, because in this case you get a reasonable period). 
The bead must be painted black matt, and placed in front of a white background (a paper sheet will do). The Raspbian distribution includes a video 
player called **omxplayer**; you may also find useful a free image displaying software such as **Mirage**. 

Before using the program **gpi**, some libraries and packages (such as GTK and OpenCV) must installed. In order to avoid any error that might affect any
further attempt to install these requirements, we use docker containers ([here](https://devopscube.com/what-is-docker/) is an overview on how docker 
works). To have docker and docker-compose installed and tested, open a terminal and run:
```console
pi@raspberry:~/rasptracking $ sudo requirements_local.sh
pi@raspberry:~/rasptracking $ docker run hello-world
```

By the end, you should have a **Hello from Docker!** message on your terminal. A common error you might face is that docker does not have the 
permissions yet to be run withouth sudo, just restart your raspberry pi and you are good to go. Next step, we allow xhost to share the devices connected
to the raspberry pi with exterior hosts and create your docker image and a container
with:
```console
pi@raspberry:~/rasptracking $ xhost + 
pi@raspberry:~/rasptracking $ docker-compose run raspbian_lab /bin/bash
```

Be patient with OpenCV; libraries may take _hours_ to install. (ETA: ~4h for the whole installation)

The program to carry out the Particle Tracking technique is called gpi.py; you start it by typing **python3 gpi.py** on a terminal. A graphical 
user interface will open.

* The **Preview** button allows to see the camera view, in order to place it and center & focus the pendulum.
* The **Background Picture** button just acquires a few still pictures of the background (_you must remove the bead_), averages them, and stores the resulting image in order to subtract it from every video frame.
* The **Record Video** button will record an mp4 video for the seconds indicated in the box _record time_, and will store it with the name indicated in the box _video name_. The PiCamera records at 25 frames (factory default). 
* The **View Video** button shows the recorded video.
* The **Track** button finds the pendulum position along time and saves the data.

A typical procedure is explained below in the LabScript.pdf document.
