FROM python:3.8.5

WORKDIR /foodgram
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
COPY . .
CMD gunicorn project.wsgi:application --bind 0.0.0.0:8000 \
    # --error-logfile error.log \
    # --access-logfile access.log \
    # --capture-output --log-level debug
