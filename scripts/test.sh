#! /bin/bash
sudo apt install python3 python3-pip python3-venv

python3 -m venv testing-venv

. testing-venv/bin/activate

pip3 install -r tests/requirements.txt

pytest --cov=service1
pytest --cov=service2

deactivate

rm -rf testing-venv