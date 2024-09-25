#!/bin/bash

source ~/ENVS/jsonserver/bin/activate
cd "$(dirname "$0")"
python load_data.py