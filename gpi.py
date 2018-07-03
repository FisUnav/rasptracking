#!usṛ/bin/python3
from guizero import App, Combo, Text, PushButton, info, MenuBar, TextBox, Picture
import os
import picamera
from picamera.array import PiRGBArray
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import cv2
import skimage
import skimage.morphology
from scipy import ndimage




#cam1=picamera.PiCamera(framerate=30)
camera=picamera.PiCamera(framerate=32,resolution = (1920, 1088))
sleep(2)
camera.shutter_speed = 10000
sleep(2)
camera.iso=800
sleep(1)

if not (os.path.isdir("dataGPI")):
	os.makedirs("dataGPI")


def focus():
	sleep(0.1)
	camera.framerate = 25
	camera.resolution = (1920, 1088)    
	#outputText.value = "Focusing"
	sleep(0.1)
	rawCapture = PiRGBArray(camera, size=(1920, 1088))
	# capture frames from the camera
	sleep(0.1)
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		# grab the raw NumPy array representing the image, then initialize the timestamp
		# and occupied/unoccupied text
		image = frame.array
	 
		# show the frame
		cv2.namedWindow("Preview, press ´q´ to quit",cv2.WINDOW_NORMAL)
		cv2.resizeWindow("Preview, press ´q´ to quit", 1024,768)
		cv2.imshow("Preview, press ´q´ to quit", image)
		key = cv2.waitKey(1) & 0xFF
	 
		# clear the stream in preparation for the next frame
		rawCapture.truncate(0)
	 
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break
	

	for i in range (1,10):
		cv2.waitKey(0)
	sleep(0.1)    
	outputText.value = "End Preview"
        

def takeBackground():
	camera.resolution = (1920, 1088)
	camera.framerate = float(fpsText.value)
	sleep(1)
	camera.exposure_mode='off'
	g = camera.awb_gains
	camera.awb_mode = 'off'
	camera.awb_gains = g
	nombrevideo = "vidfondo"
	#info("record", "it is going to record the video {0}.mp4".format(nombrevideo))
	camera.start_preview()
	camera.start_recording("dataGPI/" + nombrevideo + ".h264")
	duracion = 3.0
	camera.wait_recording(duracion)
	camera.stop_recording()
	camera.stop_preview()
	sleep(1)
	
	varOk = True
	cap = cv2.VideoCapture("dataGPI/" + nombrevideo + ".h264")
	i = 0 
	
	while(varOk):
		ret, frame = cap.read()
		
		i = i + 1
		if not ret:
			break
		if ((i==1) or (i == 21) or (i == 41) or (i == 61)):
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			if i==1 :
				fondo1=frame
			if i==21:
				fondo2=frame
			if i==41:
				fondo3=frame
			if i==61:
				fondo4=frame
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			varOk = False
	cap.release()
	cv2.waitKey(1000)
	cv2.destroyAllWindows()
	for i in range (1,10):
		cv2.waitKey(1)
	outputText.value = "End Playing"
	
	
	
	#outputText.value = "Taking Background"
	output = np.zeros((1088, 1920, 3), dtype = np.int32)
	outputf = np.zeros((1088, 1920, 3))
    #info("background","Taking background")
	output=fondo1.astype(np.int32)+fondo2.astype(np.int32)+fondo3.astype(np.int32)+fondo4.astype(np.int32)
	#import pdb; pdb.set_trace()
	outputf = (output/4)
	cv2.imwrite("dataGPI/" + "imagef.jpg", (output/4))
	imgFile = cv2.imread("dataGPI/" + 'imagef.jpg')
	cv2.namedWindow('background',cv2.WINDOW_NORMAL)
	cv2.resizeWindow('background', 1024,768)
	cv2.imshow('background', imgFile)
	for i in range(0,4):
		cv2.waitKey(0)
	cv2.destroyAllWindows()
	sleep(0.1)
	outputText.value = "Background Ready"

def recordvideo():
	
	#outputText.value = "Recording"
	camera.resolution = (1920, 1088)
	camera.framerate = float(fpsText.value)
	sleep(2)
	camera.exposure_mode='off'
	g = camera.awb_gains
	camera.awb_mode = 'off'
	camera.awb_gains = g
	nombrevideo = videoname.value
	#info("record", "it is going to record the video {0}.mp4".format(nombrevideo))
	camera.start_preview()
	camera.start_recording("dataGPI/" + nombrevideo + ".h264")
	duracion = float(timeRecording.value)
	camera.wait_recording(duracion)
	camera.stop_recording()
	camera.stop_preview()
	sleep(1)
	os.system('MP4Box -add dataGPI/{0}.h264 dataGPI/{0}.mp4'.format(nombrevideo))
	outputText.value = "End Recording"

def viewvideo():
	outputText.value = "Playing"
	nombrevideo = videoname.value
	varOk = True
	cap = cv2.VideoCapture("dataGPI/" + nombrevideo + ".h264")
	while(varOk):
		ret, frame = cap.read()
		if not ret:
			break
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
		cv2.resizeWindow('frame', 1024,768)
		cv2.imshow('frame',gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			varOk = False
	cap.release()
	cv2.waitKey(1000)
	cv2.destroyAllWindows()
	for i in range (1,10):
		cv2.waitKey(1)
	outputText.value = "End Playing"

    
    
    
    

def select():
    os.chdir(browserDir.value)
    dirs = [item for item in list(os.walk("."))[0][1] if not item.startswith(".")] 
    browserDir.clear()
    browserDir.add_option("..")
    for ii in dirs: 
       browserDir.add_option(ii)
    for ii in os.listdir():
       if ii.endswith(".mp4"):
           browserDir.add_option(ii)
    #print(os.getcwd())

    
def track():
	### params #################################
	umbral=float(umbralText.value)  # nivel de gris, del 0 al 255
	radio=float(radioText.value)    # radio del disco para erosionar
	fps=float(fpsText.value)      # fotogramas por segundo del vídeo
	L=float(lText.value)      # longitud de la cuerda

	# recorte de la imagen: 
	# el eje vertical es POSITIVO HACIA ABAJO
	abajo=float(downText.value)   # porción de ARRIBA de la imagen
	arriba=float(upText.value)  # porción de ABAJO de la imagen
	# mejor si son múltiplos de 4

	### ==== cálculos =========================#
	strel = np.ones((radio,radio),np.uint8)
	############################################
	#outputText.value = "Tracking"
	nombrevideo=videoname.value + ".h264"
	### lectura del vídeo
	cap = cv2.VideoCapture("dataGPI/" + nombrevideo)
	if (cap.isOpened()== False): 
	  print("Error al abrir el vídeo")

	### imagen del fondofondo
	#backGround0 ='fondokk25.jpg'
	backGround0 ="dataGPI/" + "imagef.jpg"
	imfondo = cv2.imread(backGround0)
	imfondogr=cv2.cvtColor(imfondo,cv2.COLOR_BGR2GRAY)
	imfondog=imfondogr[abajo:arriba,:]

	### ventanas
	cv2.namedWindow('video',cv2.WINDOW_NORMAL)
	cv2.moveWindow('video',10,10)
	cv2.resizeWindow('video', 480,270)

	cv2.namedWindow('tracking video',cv2.WINDOW_NORMAL)
	cv2.moveWindow('tracking video',10,320)
	b = int((arriba-abajo)/4)
	cv2.resizeWindow('tracking video', 480, b)

	# bucle para detectar la posición del péndulo
	# en cada faotograma del video

	centros=[]
	contaframe=1 
	#while(True):
	while(contaframe<1000):
	  ret, frame = cap.read()
	  contaframe=contaframe+1
	  if ret == True:
	     imactualg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	     imactual = imactualg[abajo:arriba,:]
	     im3=cv2.subtract(imfondog,imactual)          
	     im4b=im3>umbral
	     im5b=cv2.morphologyEx(np.uint8(im4b), cv2.MORPH_OPEN, strel)    
	     cv2.imshow('video',frame)
	     cv2.imshow('tracking video', np.uint8(im5b*255))
	     (x1,y1) = ndimage.measurements.center_of_mass(im5b)
	     centros.append((contaframe,y1))
	     #print(contaframe)
	     
	     if cv2.waitKey(25) & 0xFF == ord('q'): break

	  else:
	    break

	print("Vídeo Acabado")

	cap.release()
	cv2.waitKey(100) & 0xFF
	cv2.destroyAllWindows()
	for i in range (1,10):
         cv2.waitKey(1)
	# procesado de la posición
	# para hallar T, luego g

	centros=np.array(centros)
	t=centros[:,0]/fps
	x=centros[:,1]
	XMed=((max(x)+min(x))/2)
	x=x-XMed

	fig,ax1=plt.subplots(figsize=(10,10))

	# para Windows solamente
	#gestor=plt.get_current_fig_manager()
	#gestor.window.setGeometry(10,450,600,400)

	ax1.plot(t,x,'r.',t,x,'r')

	contaframe=contaframe-1
	pasosabajo=[]
	pasosarriba=[]
	for contador in range(1,contaframe-1):
		if ((x[contador-1]*x[contador])<0):
			if (x[contador]>0):
				tinter=[t[contador-1],t[contador]]
				rinter=[x[contador-1],x[contador]]
				tpaso=np.interp(0,rinter,tinter)
				pasosarriba.append((tpaso,0))
			elif (x[contador]<0):
				#print(contador)
				tinter=[t[contador],t[contador-1]]
				rinter=[x[contador],x[contador-1]]
				tpaso=np.interp(0,rinter,tinter)
				pasosabajo.append((tpaso,0))
			else:
				print('raro')
				
				
	parriba=np.array(pasosarriba)
	pabajo=np.array(pasosabajo)
	ax1.plot(parriba[:,0],parriba[:,1],'b.')
	ax1.plot(pabajo[:,0],pabajo[:,1],'g.')
				
	s1=np.diff(parriba[:,0])
	s2=np.diff(pabajo[:,0])            
			
	T=np.append(s1,s2)
	g=4*(np.pi**2)*L/(np.mean(T)**2)
	errorg=g*(0.001*(2/L)+(2*np.std(T)/np.mean(T)))

	#print('valor de g')
	#print(g)
	#print('error')
	#print(errorg)
		
	# para raspberry ...
	#sleep(2)
	np.savetxt("dataGPI/" + "periods.dat", T)
	
	fileXvsT = open("dataGPI/" + "xvst.dat","w")
	for index in range(len(x)):
		fileXvsT.write(str(t[index]) + " " + str(x[index]) + "\n")
	fileXvsT.close()
	plt.savefig("dataGPI/" + "plot.png", bbox_inches = "tight")#block=False
	sleep(2)
	imgFile = cv2.imread("dataGPI/" + 'plot.png')
	cv2.imshow('Oscilations', imgFile)
	for i in range(0,4):
		cv2.waitKey(0)
	cv2.destroyAllWindows()
	sleep(0.1)
	outputText.value = "End Tracking"
	#graf=Picture(app, image="plot.png", grid = [0,4])
	#sleep(5)
	#mngr=plt.get_current_fig_manager()
	#sleep(2)
	#mngr.window.wm_geometry("+10+200")
	#sleep(2)
	#input("Press Enter to continue...")

 
app = App(title = "gpi", width = 650, height = 250, layout = "grid")
dirs = [item for item in list(os.walk("."))[0][1] if not item.startswith(".")]

videoname = TextBox(app, grid=[1 , 3], align="left")
videoname.value = "videoname"

labelVN = Text(app, grid=[0 , 3], text = "video name",align="left")

wdText = Text(app, grid=[1 , 0], text = "folder",align="left")

timeRecording = TextBox(app, grid=[1 , 5], align="left")
timeRecording.value = "3"
labelTime = Text(app, grid=[0 , 5], text = "record time",align="left")

browserDir = Combo(app, options = dirs, command=select, grid=[0,0], align="left")

parametersText = Text(app, grid=[1 , 6], text = "Parameters",align="left")

umbralText = TextBox(app, grid=[1 , 7], align="left")
umbralText.value = "100"
umbralLabel = Text(app, grid=[0 , 7], text = "Treshold",align="left")

radioText = TextBox(app, grid=[3 , 7], align="left")
radioText.value = "30"
radiolLabel = Text(app, grid=[2 , 7], text = "Radius",align="left")

fpsText = TextBox(app, grid=[1 , 8], align="left")
fpsText.value = "25"
fpsLabel = Text(app, grid=[0 , 8], text = "fps",align="left")

lText = TextBox(app, grid=[3 , 8], align="left")
lText.value = "0.54"
lLabel = Text(app, grid=[2 , 8], text = "Longitud",align="left")

outputText = Text(app, grid=[3 , 5], text = "Output",align="left")

upText = TextBox(app, grid=[5 , 7], align="left")
upText.value = "800"
upLabel = Text(app, grid=[4 , 7], text = "down",align="left")

downText = TextBox(app, grid=[5 , 8], align="left")
downText.value = "400"
downlLabel = Text(app, grid=[4 , 8], text = "up",align="left")

for ii in os.listdir():
    if ii.endswith(".mp4"):
           browserDir.add_option(ii)

enfocar = PushButton(app, text = "Preview" ,command = focus, grid=[0,1], align="left")
background = PushButton(app, text = "Background Picture" ,command = takeBackground, grid=[1,1], align="left")
#setButton = PushButton(app, text = "Set Parameters" ,command = setParameters , grid=[5,1], align="left")
record = PushButton(app, text = "Record Video" ,command = recordvideo, grid=[2,1], align="left")

view = PushButton(app, text = "view video" ,command = viewvideo, grid=[3,1], align="left")
trackButton = PushButton(app, text = "track" ,command = track , grid=[4,1], align="left")


app.display()
