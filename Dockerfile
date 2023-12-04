FROM python:3.12.0-alpine3.18
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers libffi-dev

COPY ./requirements.txt ./requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install pip --upgrade \
    && pip install -r requirements.txt

COPY ./src ./src/

EXPOSE 8000

CMD [ "python", "./src/manage.py", "runserver", "0.0.0.0:8000"]