FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk update                      \
&& pip install --no-cache-dir pyotp

WORKDIR /usr/src/app
COPY ./src .
ENTRYPOINT [ "python3", "app.py" ]