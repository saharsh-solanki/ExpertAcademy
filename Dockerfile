FROM ubuntu
RUN apt-get update
RUN apt-get install python3-dev python3-setuptools python3-pip -y
RUN pip install --upgrade pip
RUN apt install python3.10-venv -y
RUN apt-get install libtiff5-dev libjpeg8-dev -y
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
ENTRYPOINT python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000