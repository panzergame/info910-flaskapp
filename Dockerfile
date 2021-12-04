FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y libmariadb-dev-compat gcc

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000
COPY . .
CMD [ "python3", "app.py"]
