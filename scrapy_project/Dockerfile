FROM python:3.12.0-alpine3.18
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers libffi-dev \
    && pip3 install --no-cache-dir scrapy pymongo

COPY ./scrapy_project ./

CMD [ "python3", "run.py" ]