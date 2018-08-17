sudo apt-get update
sudo apt-get install -y python3 python3-pip x11-server-utils
cd ~/
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo groupadd docker
sudo pip3 install docker-compose 
newgrp docker
