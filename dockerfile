FROM python:3

WORKDIR /app

COPY . /app

CMD ["pip", "install", "-r", "requirements.txt"]

RUN python -m main.py