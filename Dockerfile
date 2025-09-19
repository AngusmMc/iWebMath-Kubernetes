# use python as the base image
FROM python:3.10.12 

# create the working directory called app inside the container
WORKDIR /app 

# copy the requirements file into the container
COPY requirements.txt requirements.txt

# run the command to install the dependencies
RUN pip3 install -r requirements.txt

# copy the flask app.py file into the container
COPY app.py app.py

# run these commands when the container starts to run the app
CMD [ "python3", "app.py"]

