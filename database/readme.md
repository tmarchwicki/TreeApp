# Install Docker/Docker compose
sudo bash install_docker.sh
sudo bash run.sh

# Install Python
sudo apt install python3-pip
source deactivate

# Install requirements
pip install -r requirements.txt

# load data
bash load_data.sh
