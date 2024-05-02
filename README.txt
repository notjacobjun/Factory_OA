# Setup instructions
Python 3.9+ (required)

## Virutal Environment setup (make sure that you are using python3 and that you have python 3.9 installed)
#------FOR LINUX/MAC---------#

#NOTE venv should be included for python 3.9 and above (however if it isn't then install using homebrew or apt-get for mac and linux respectively)

#creating virtual env

python3 -m venv env

#activating virtual env

source env/bin/activate


#-------FOR WINDOWS----------#

#NOTE venv should be included with python 3.9 and above by default however if it isn't then install it on windows using the command below

py -m pip install --user virtualenv

#creating virtual env

py -m venv env

#activating virtual env

.\env\bin\activate

## Instructions for both mac/linux/windows once you have setup the virtual environment (API setup)
#install the api sdk for gemini
pip install -r requirements.txt
