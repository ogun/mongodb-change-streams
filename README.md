# Requirements

python3, docker

# How to run

Run the following command:
- python3 -m venv venv
- source ./venv/bin/activate ([for windows: (venv folder)\Scripts\Activate.ps1](https://docs.python.org/3/library/venv.html))
- pip install -r requierments.txt
- docker-compose -f docker-compose.mongodb.yaml up -d
