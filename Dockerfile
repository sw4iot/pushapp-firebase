FROM python:3.6-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pushapp_firebase/ .
COPY app.py .

CMD [ "python", "app.py" ]