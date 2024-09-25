#!/bin/bash

cd "$(dirname "$0")"
npm run build
serve -s build -l 3004