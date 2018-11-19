sudo docker network create test_network
sudo docker run -diP --rm --name main mainentry
sudo docker run -di --rm --name py_model_1 pythonentry
sudo docker run -di --rm --name r_model_1 rentry
sudo docker network connect test_network main
sudo docker network connect test_network py_model_1
sudo docker network connect test_network r_model_1
sudo docker ps -a
