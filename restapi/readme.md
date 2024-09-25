# Install Python
sudo apt install python3

# Install environment
mkdir -p ~/ENVS
cd ~/ENVS
python3.10 -m venv jsonserver

# How to install
source ~/ENVS/jsonserver/bin/activate

cd ~/code/app/restapi
pip install -r requirements.txt

# How to run
bash run.sh

# should be available under the url: 
http://127.0.0.1:8000/tree
http://127.0.0.1:3004/tree

# testing
pytest --rootdir=.

# kill
kill-port 3004
