FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install flask && pip3 install flask-restful
COPY ./app/app.py app.py
EXPOSE 5000
CMD ["python3", "app.py"]
