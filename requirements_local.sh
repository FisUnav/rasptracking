sudo apt-get update
sudo apt-get install -y python3 python3-pip
cd ~/
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo groupadd docker
newgrp docker
sudo pip3 install docker-compose 
