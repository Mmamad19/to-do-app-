 FROM python:3.8-slim-buster

 ENV PYTHONUNBUFFERED 1
 ENV PYHONDONTWRITEBYTECODE 1
 WORKDIR /code
 COPY requirements.txt /code/

 RUN  pip3 install --upgrade pip
 RUN pip3 install -r requirements.txt
 ADD ./core /code/

 CMD [ "python3","manage.py","runserver","0.0.0.0:8000" ]
