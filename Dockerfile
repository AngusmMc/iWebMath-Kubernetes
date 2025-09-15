FROM python:3.10.12
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app.py app.py
CMD [ "python3", "app.py"]