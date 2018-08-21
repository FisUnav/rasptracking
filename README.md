# Rasptracking #

This repository contains code and instructions for an implementation of a Particle Tracking system with a Raspberry Pi nanocomputer and a Picamera. 

The idea is to use a Raspberry Pi + Picamera to carry out the well-known pendulum experiment. It involves measuring the pendulum period, and calculating the value of _**g**_, the gravity acceleration. This can be done by hand with a chronometer, of course. A Particle Tracking technique will automate the procedure.

In order to accomplish this, a video must be recorded of the pendulum motion. A dark pendulum over a white background is needed). A simple image processing allows to obtain the pendulum position at every frame. Plotting the position over time will show a sinusoid; from the zero crossings, the period is readily obtained.

The program allows to do the following: to record a video of the pendulum motion; to capture a still picture of the background (it will be subtracted to each frame); to analize the video in order to obtain the position at every frame; and to save the period data.

The files in this repository are:
* _readme.md_ : this file.
* _Installation.md_ : a concise documentation explaining how to prepare the hardware and software needed. 
* _gpy.py_ : the code ready to run and perform the above tasks. It is written in Python.
* _LabScript.pdf_ : a laboratory session script intended for first year college students, demonstrating the program features in a typical procedure.
* _iconGPI.png_ : an icon (which is not really needed to run the program).
* _Dockerfile_: A Dockerfile with all the requirements to run the program in a docker container.
* _docker-compose.yml_: A docker-compose file with all the specifications to create a container enable to access the PICamera and persist data in the folder **/home/pi/Desktop/datos_practicas/**.
* _config.txt_: A config file for the camera options to be copied into the container.
* _requirements.txt_ : All python requirements to be installed with Python pip (those packages cannot be installed from python3 source). 
* _requirements_local.sh_: Requirements to install docker and docker-compose.

If you want to get the system running, you should download all these files to a [Raspberry Pi 3 model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) running in Raspbian and supplemented with a [Raspberry Pi Camera Module v2](https://www.raspberrypi.org/products/camera-module-v2/). Then follow the steps indicated in the file Installation.md.
