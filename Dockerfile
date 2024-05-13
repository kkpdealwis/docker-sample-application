FROM python:3.9
WORKDIR /app

COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir requirements.txt

COPY ./app .

CMD [ "python","app.py" ]