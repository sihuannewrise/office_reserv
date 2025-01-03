FROM python:3.12.5-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt client.py /app/

WORKDIR /app

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["python", "client.py"]
