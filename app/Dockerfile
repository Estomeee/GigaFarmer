FROM python:3.9

WORKDIR ./code/app
WORKDIR ../

COPY ./requirements.txt /code/app/requirements.txt

COPY ./text.txt /code/app/text.txt

RUN pip install --no-cache-dir --upgrade -r /code/app/requirements.txt

COPY ./config.py ./main.py /code/app

COPY ./main.py /code

COPY . /code/app