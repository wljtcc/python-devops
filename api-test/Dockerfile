# base python image for custom image
FROM python:3.10.14-alpine3.18

# create working directory and install pip dependencies
WORKDIR /api
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy python project files from local to /hello-py image working directory
COPY . .

# run the flask server  
CMD [ "python3", "main.py"]