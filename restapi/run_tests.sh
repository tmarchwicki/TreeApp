#!/bin/bash

source ~/ENVS/jsonserver/bin/activate
cd "$(dirname "$0")"
pytest --rootdir=.