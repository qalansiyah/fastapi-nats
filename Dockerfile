FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y sqlite3

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

COPY count.db .
COPY count_and_avg.so .
COPY data.json .

CMD ["uvicorn", "main:webapp", "--host", "0.0.0.0", "--port", "8888", "--log-level", "debug"]
