FROM python:3.10.3
WORKDIR /
COPY requirements.txt requirements.txt
CMD [ "python3", app.py]