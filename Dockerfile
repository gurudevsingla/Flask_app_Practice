FROM python:3.8.19-slim

WORKDIR /flask-docker


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3","-m","flask","run","--host=0.0.0.0"]