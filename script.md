El material empleado es: una Raspberry Pi 3B, con carcasa y picamera, que corre en Raspbian; y un péndulo construido con una esfera de plomo de 1 cm. de radio, colgando de un hilo de 54 cm. de largo, pintado de negro, situado delante de una superficie clara.
Con Raspbian viene un programa llamado omxplayer que permite visualizar vídeos, e instalamos también Mirage, un programa gratuito para visualizar imágenes. 
La Raspberry Pi debe prepararse instalando algunas algunas librerías, como GTK y OpenCV. Todo ello se logra ejecutando el bash "requirements.sh". Hay que tener paciencia con las librerías OpenCV, que pueden tardar _horas_ en instalarse.
El programa se lanza ejecutando en una terminal la orden **python3 gpi.py**, que abre una interfaz gráfica de usuario.
El botón **Preview** permite ver lo que graba la cámara, para centrar y enfocar el péndulo.
El botón **Background Picture** toma unas pocas fotografías del fondo (_retirar el péndulo_) para calcular el promedio. Esa imagen se restará después a cada fotograma del vídeo.
El botón **Record Video** graba un vídeo encapsulado en mp4 con la duración en segundos indicada en la casilla _record time_ y con el nombre que se escriba en la casilla _video name_. La picamera graba a 25 frames per second. 
Con el botón **View Video** se visualiza el vídeo grabado.
El botón **Track** halla la posición del péndulo a lo largo del tiempo.

A continuación se explica brevemente el procedimiento típico.
