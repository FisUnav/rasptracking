# Rasptracking #

This repository contains code and instructions for an implementation of a Particle Tracking system with a Raspberry Pi nanocomputer and a Picamera. 

The idea is to use a Raspberry Pi + Picamera to carry out the well-known pendulum experiment. It involves measuring the pendulum period, and calculating the value of g, the gravity acceleration. This can be done by hand with a chronometer, of course. A Particle Tracking technique will automate the procedure.

In order to accomplish this, a video must be recorded of the pendulum motion. A dark pendulum over a white background is needed). A simple image processing allows to obtain the pendulum position at every frame. Plotting the position over time will show a sinusoid; from the zero crossings, the period is readily obtained.

The program allows to do the following: to record a video of the pendulum motion; to capture a still picture of the background (it will be subtracted to each frame); to analize the video in order to obtain the position at every frame; and to save the period data.

The files in this repository are:
* readme.md : this file.
* gpy.py : the code ready to run and perform the above tasks. It is written in Python.
* requirements.sh : All python requirements to be installed with Python pip (those packages cannot be installed from python3 source).
* script.md : a concise documentation explaining the program features and how to use it. 
* LabScript.pdf : a laboratory session script intended for first year students. _Note that much of_ scritpt.md _and_ LabScript.pdf _are the same material_.
* iconGPI.png : an icon (which is not needed to make the program run).
* Dockerfile: A Dockerfile with all the requirements to run the program in a docker container.
* docker-compose.yml: A docker-compose file with all the specifications to create a container enable to access the PICamera and persist data in the folder **/home/pi/Desktop/datos_practicas/**.
* config.txt: A config file for the camera options to be copied into the container.
