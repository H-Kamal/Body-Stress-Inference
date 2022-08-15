# Python files
This folder contains the necessary python files to run the backend part of the project.

- main.py: This file runs the backend code on the python side which allows for motion capture of the user with blazepose.
- pose.py: This file contains the code to perfrom motion capture with blazepose and openCV.
- calcUtilities.py: This file contains the functions which allow us to calculate the angles of the body parts for REBA analysis.
- rebaAnalysis.py: This file contains the code to calculate the REBA score for various body parts.
- server.py: This file contains the functions which allow us to open a socket connection from python to unity and send the data to unity to be displayed.