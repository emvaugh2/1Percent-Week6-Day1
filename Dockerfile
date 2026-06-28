# This is our Dockerfile

FROM python:3.9-slim 
WORKDIR /greeting_server 
COPY greeting_server.py /greeting_server 
COPY requirements.txt /greeting_server 
RUN pip install -r requirements.txt 
EXPOSE 5000
CMD ["python", "greeting_server.py"]  