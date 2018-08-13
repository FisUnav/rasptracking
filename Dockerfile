FROM resin/rpi-raspbian:latest
MAINTAINER José Ilberto (jfonceca@alumni.unav.es)

ENV RUNTIME_PACKAGES python3 python3-pip cmake pkg-config bash ca-certificates wget unzip
ENV BUILD_PACKAGES build-essential libavcodec-dev libavformat-dev \
		libswscale-dev libv4l-dev libxvidcore-dev libx264-dev \
		libgtk2.0-dev libatlas-base-dev libjpeg8 libjpeg8-dev \
		libopenjpeg5 zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev \
		tcl8.5-dev tk8.5-dev imagemagick gfortran \
		python2.7-dev python3-dev python3-setuptools python3-tk \ 
		python3-skimage python3-picamera python3-matplotlib \
		raspi-config git


ADD . /home/pi/rasptracking/
ADD /boot/config.txt /boot/
WORKDIR /home/pi/
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install $RUNTIME_PACKAGES
RUN wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip && \
         unzip opencv.zip && rm opencv.zip && \
         wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip && \
         unzip opencv_contrib.zip && rm opencv_contrib.zip
RUN apt-get install $BUILD_PACKAGES && \
	pip3 install -r ./rasptracking/requirements.txt && \
	update-ca-certificates && \
	apt-get autoremove
	
RUN cd opencv-3.1.0/ && mkdir build/ && cd build && \
	cmake -D MAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D OPENCV_EXTRA_MODULES_PATH=/home/pi/opencv_contrib-3.1.0/modules \
        -D BUILD_EXAMPLES=ON .. && \
	make -j2 && \
	make install && ldconfig
	
