python -m venv env # establishes the virtual environment called env
source env/bin/activate # activates the venv

# check activation
which python # should be in ./env/bin/python
which pip # should be in ./env/bin/pip

# install dependencies
pip install --upgrade pip # updates pip
pip install -r requirements.txt
pip list # lists packages
pip freeze > requirements.txt # saves package list with versions to ./requirements.txt