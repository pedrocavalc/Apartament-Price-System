FROM python:3.10.13-bullseye
WORKDIR /app
COPY . .

RUN apt-get update && \
pip3 install -r requirements.txt 

EXPOSE 5000

CMD ["mlflow", "server", "--host", "0.0.0.0", "--backend-store-uri", "sqlite:///mlflow.db", "--default-artifact-root", "file:///mlflow-artifacts"]