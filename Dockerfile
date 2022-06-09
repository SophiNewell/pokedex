FROM python:3.7-buster

RUN mkdir -p /opt/app
COPY requirements.txt /opt/app/
WORKDIR /opt/app/
RUN pip install -r requirements.txt
COPY pokedex pokedex
CMD ["python","pokedex/manage.py","runserver","0.0.0.0:8000"]