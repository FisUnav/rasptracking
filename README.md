# Rasptracking #

Este repositorio contiene el código para una implementación de Particle Tracking con una Raspberry Pi y su cámara (picamera). 

La idea es emplear una Raspberry Pi y una picamera para realizar el experimento clásico del péndulo (en el cual se obtiene el valor de  g, la aceleración de la gravedad, midiendo el período), pero de manera automática.

Para ello, se registra en vídeo el movimiento de un péndulo oscuro sobre fondo blanco. Mediante un tratamiento de imágenes sencillo se obtiene la posición del péndulo en cada fotograma; y graficando las posiciones del péndulo a lo largo del tiempo, se obtiene una sinusoide, de la cual se calcula el período.
El programa permite: registrar un vídeo del péndulo; tomar una fotografía del fondo (esta imagen se resta a cada fotograma); analizar el vídeo para encontrar la posición de cada fotograma; y guardar los datos. 

Los archivos son:
* gpi.py : el código del programa para implementar la técnica de particle tracking, escrito en Python.
* LabScript.pdf : un guión de prácticas explicado para los alumnos de primero que realizan esta práctica.
* requirements.sh : archivo bash para instalar las librerías y software necesario.
* iconGPI.png : un icono (no es necesario).
* script.md : una breve documentación para explicar el funcionamiento del programa.
