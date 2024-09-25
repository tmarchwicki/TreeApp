# Install Python
sudo apt install python3

# Install requirements
pip install -r requirements.txt

# Start server
bash run.sh

# Server should be available under the url: 
http://127.0.0.1:8000/tree

# unit test
pytest --rootdir=.
