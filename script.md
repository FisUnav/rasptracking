El material empleado es: una Raspberry Pi 3B, con carcasa y picamera, que corre en Raspbian; y un péndulo construido con una esfera de plomo de 1 cm. de radio, colgando de un hilo de 54 cm. de largo, pintado de negro, situado delante de una superficie clara.
Con Raspbian viene un programa llamado omxplayer que permite visualizar vídeos, e instalamos también Mirage, un programa gratuito para visualizar imágenes. 
La Raspberry Pi debe prepararse instalando algunas algunas librerías, como GTK y OpenCV. Todo ello se logra ejecutando el bash "requirements.sh". Hay que tener paciencia con las librerías OpenCV, que pueden tardar _horas_ en instalarse.
El programa se lanza ejecutando en una terminal la orden **python3 gpi.py**, que abre una interfaz gráfica de usuario.

* El botón **Preview** permite ver lo que graba la cámara, para centrar y enfocar el péndulo.
* El botón **Background Picture** toma unas pocas fotografías del fondo (_retirar el péndulo_) para calcular el promedio. Esa imagen se restará después a cada fotograma del vídeo.
* El botón **Record Video** graba un vídeo encapsulado en mp4 con la duración en segundos indicada en la casilla _record time_ y con el nombre que se escriba en la casilla _video name_. La picamera graba a 25 frames per second. 
* Con el botón **View Video** se visualiza el vídeo grabado.
* El botón **Track** halla la posición del péndulo a lo largo del tiempo.

A continuación se explica brevemente el procedimiento típico. (En el documento LabScript.pdf está explicado también).

The camera is focused at 50 cm. Place the camera at such a distance from the pendulum. Set the white screen behind the pendulum. Lighting is of crucial importance; use natural light if possible and avoid the shadow of the sphere as much as possible.
You will take an image of the background, without the pendulum. After that, you will want a short (~4 seconds) video to test that everything is working fine. Once you have fixed the system variables, you will record a longer (20 seconds) video. The program will then track the bead and provide you the measurements for the period.
Proceed by completing the following steps.
1.	Open a terminal by clicking on the terminal icon:
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
