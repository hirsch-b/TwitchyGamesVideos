FROM python:3.12-slim

WORKDIR /opt

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir
COPY twitchybackend/ /opt/twitchybackend

EXPOSE 8000

CMD [ "fastapi", "run", "twitchybackend/app.py" ]
