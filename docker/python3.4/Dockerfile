FROM python:3.4.3

RUN pip install --no-cache-dir \
    numpy==1.8.2 \
    flake8 \
    autopep8

COPY ./ /workspace

WORKDIR /workspace