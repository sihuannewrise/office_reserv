# scp Dockerfile sihuan@192.168.2.91:~/auth
FROM python:3.12.5-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# adding root CAcert to image
COPY RootCA.crt /usr/local/share/ca-certificates/
RUN apt-get update && apt-get install -y ca-certificates
RUN update-ca-certificates

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir

COPY main.py /app/

CMD ["fastapi", "run", "main.py", "--port", "8001", "--proxy-headers"]
