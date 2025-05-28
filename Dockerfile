FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
RUN apt-get update && apt-get install -y nano
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
