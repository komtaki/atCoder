FROM python:3.8.2-slim

RUN apt-get update && apt-get install -y git

RUN pip install --no-cache-dir \
    numpy==1.18.0 \
    scipy==1.4.1 \
    scikit-learn==0.22 \
    numba==0.47.0 \
    networkx==2.4 \
    flake8 \
    autopep8

RUN mkdir /workspace

WORKDIR /workspace