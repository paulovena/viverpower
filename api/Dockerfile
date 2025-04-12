FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install streamlit psycopg2 pandas

CMD ["streamlit", "run", "app.py", "--server.port=80", "--server.enableCORS=false"]
