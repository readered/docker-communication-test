sudo docker network create test_network
sudo docker run -diP --rm --name main mainentry
sudo docker run -di --rm --name secondary secondentry
sudo docker network connect test_network main
sudo docker network connect test_network secondary
sudo docker ps -a
