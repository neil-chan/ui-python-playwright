FROM mcr.microsoft.com/playwright/python:next-jammy-arm64
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
RUN playwright install --with-deps