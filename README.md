# ENSC482
Project interfacing webcam with image recognition and graphic output for ENSC 482. Contributors are Hamza Kamal, Kirill Melnikov, and Roy Ataya.


# Installing Dependencies Instructions:
## Using Poetry
1. Clone this repository
2. Navigate to the repository
3. Check if you have Poetry installed on your machine through `poetry --version`
   1. If you don't have Poetry installed, install it through following these instructions: [Install Poetry](https://python-poetry.org/docs/#installation)
   2. If you have Poetry installed, run `poetry install` in the repository's root.

## Using Pip
1. Run the following commands to install all the required python packages for the project:
   1. `pip install opencv-python==4.6.0.66`
   2. `pip install mediapipe==0.8.10.1`
   3. `pip install numpy==1.23.0`

# Run Instructions:
1. Open unity and import the project labelled: body-stress-inference
2. Press run in unity to start the "game"
3. In terminal/CMD navigate to the cloned repo
4. Once in the folder /Body-Stress-Inference run the following command: `poetry run python body-stress-inference-python/main.py`
