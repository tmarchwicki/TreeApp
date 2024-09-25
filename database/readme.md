# run server
sudo bash install_docker.sh
sudo bash run.sh

# optional
sudo apt install python3-pip
source deactivate

# delete the old data (if needed)
cd ~/code/app/database
sudo rm -rf neo4j_db/data/

# load data
source ~/ENVS/jsonserver/bin/activate
pip install -r requirements.txt
bash load_data.sh