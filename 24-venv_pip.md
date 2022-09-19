# How to create a requirement.txt to repeat a common PIP
> Ref: https://docs.python.org/3/library/venv.html
> Ref: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment

## Find which python is installed and where
which python

## Install venv
> venv is included in the Python standard library and requires no additional installation.

## Then create a new virtual environment called venv and activate it:
> Add an -m flag to specify what version of Python runtime
> Common name for the target directory is ./venv)
python3 -m venv /path/to/new/virtual/environment


## Activate a new virtaul environment and install PIP
source venv/bin/activate
pip install scipy
pip install pandas

## You can then save these to a file by entering:
pip freeze > requirements.txt

## Now, deactivate the virtual environment and delete the venv directory:
deactivate
rm -rf venv/

## Then create a new virtual environment called venv2 and activate it:
python3.5 -m venv venv2
source venv2/bin/activate

## And now we can install all the dependencies we saved by entering:
pip install -r requirements.txt

## List 
pip freeze

## deactivate the venv
deactivate

