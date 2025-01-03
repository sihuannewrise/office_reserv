FROM python:3.12.5-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# adding root CAcert to image
COPY ca.crt /usr/local/share/ca-certificates/
RUN apt-get update && apt-get install -y ca-certificates
RUN update-ca-certificates

COPY requirements.txt client.py /app/

WORKDIR /app

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["python", "client.py"]
