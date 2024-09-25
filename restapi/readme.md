# Install python on Ubuntu
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

sudo apt install python3.10 python3.10-venv python3.10-dev
python3 --version

# Install environment
mkdir -p ~/ENVS
cd ~/ENVS
python3.10 -m venv jsonserver

# How to install
source ~/ENVS/jsonserver/bin/activate

cd ~/code/app/restapi
pip install -r requirements.txt

# How to run
source ~/ENVS/jsonserver/bin/activate
cd ~/code/app/restapi
uvicorn main:app --reload --port 8000
or
uvicorn main_neo4j:app --reload --port 8000

# should be available under the url: 
http://127.0.0.1:8000/tree
http://127.0.0.1:3004/tree

# testing
pytest --rootdir=.

# kill
kill-port 3004