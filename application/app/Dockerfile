FROM python:3.10.13-bullseye
WORKDIR /app

RUN apt-get update && \
apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0" , "--port", "8000" ]