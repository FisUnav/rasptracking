The hardware you need is a Raspberry Pi 3 model B, with a Pi Camera (a box is optional), running on Raspbian; and a pendulum which can be made with a lead bead of about 1 cm. radius, hanging from a thread (a half a meter long thin thread is suitable, because in this case you get a reasonable period). The bead must be painted black matt, and placed in front of a white background (a paper sheet will do). The Raspbian distribution includes a video player called **omxplayer**; you may also find useful a free image displaying software such as **Mirage**. 

Before using the program **gpi**, some libraries and packages (such as GTK and OpenCV) must installed. All this is accomplished with the commands in the bash file **requirements.sh**. Be patient with OpenCV; libraries may take _hours_ to install.

The program to carry out the Particle Tracking technique is called gpi.py; you start it by typing **python3 gpi.py** on a terminal. A graphical user interface will open.

* The **Preview** button allows to see the camera view, in order to place it and center & focus the pendulum.
* The **Background Picture** button just acquires a few still pictures of the background (_you must remove the bead_), averages them, and stores the resulting image in order to subtract it from every video frame.
* The **Record Video** button will record an mp4 video for the seconds indicated in the box _record time_, and will store it with the name indicated in the box _video name_. The PiCamera records at 25 frames (factory default). 
* The **View Video** button shows the recorded video.
* The **Track** button finds the pendulum position along time and saves the data.

A typical procedure is explained below. (Remark that in the LabScript.pdf document you can also find a similar explanation).

The camera is focused at 50 cm. Place the camera at such a distance from the pendulum. Set the white screen behind the pendulum. Lighting is of crucial importance; use natural light if possible and avoid the shadow of the sphere as much as possible.
You will take an image of the background, without the pendulum. After that, you will want a short (~4 seconds) video to test that everything is working fine. Once you have fixed the system variables, you will record a longer (20 seconds) video. The program will then track the bead and provide you the measurements for the period.
Proceed by completing the following steps.
1.	Open a terminal by clicking on the terminal icon.
2.	Type python3 gpi.py to launch the program (it has a graphical interface with several buttons).
3.	Place the pendulum in front of the camera, at 50 cm. Put the white screen behind the pendulum. You can visualize the field by pressing the Preview button. Once you are satisfied with the lighting, the image setting and framing, take care not to change the setup (camera, pendulum, light) until you finish. If you change it, you may have to start anew.
Close the preview window by clicking on the window bar, then press q, and close the window with the close button.
Remark.- It is important that you close the windows that display graphical output once they are not needed any more. 
4.	Lift the thread of the pendulum to take it out of the image entirely and press Background Picture to take a still photograph of the background (it will take some seconds; the image will be displayed and automatically saved under the name imagef.jpg; you can see how it looks by double clicking on it). All the output will be stored in the folder dataGPI. Close the image preview by clicking the close button.
5.	Tilt a little bit the pendulum mass and release it, just like in a grandfather clock. Do it in such a way that the oscillation takes place in a plane perpendicular to the camera line of view.
6.	Write a name for the video file in the _video name_ box, type 4 seconds in the record time and take a video by pressing Record Video. You can view it once recording has finished by pressing view video. The view and record windows must not be closed before finishing. You have to wait until it ends.
7.	Try to implement the tracking with this short video in the following way. First, select _up_ and _down_, which are the location of the vertical sides of a rectangle that must encompass the pendulum motion (the camera vertical dimension is 1080 pixels). Then select a _Threshold_ to separate the frames into black and white images so that the hanging mass is the only object visible. This is done by trial and error (threshold must be between 1 and 255). Press the track button to see the results. The track window must not be closed before finishing. Wait until tracking finishes and then close the window. Repeat until the tracking is successful.
The camera speed _fps_ must be 25 unless the camera is reconfigured. _Radius_ is meant to be the dimension of the body, and _Longitud_ the length of the thread (it’s not used here).
8.	Once you are satisfied with the results, take a 20 seconds video recording by writing a different name in the video name box, enter 20 seconds in the record time, and press the Record Video button. View the video, and then perform the tracking. The program will produce several files. One of them is **periods.dat**, which contains the measurements of the pendulum period.
9.	You may now quit the program by clicking on the close button.
10.	Insert a USB memory, and copy the files to the USB: imagef.jpg, periods.dat, xvst.dat, and your video.
