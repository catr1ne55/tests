FROM python:3
ADD app /app
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && pip install -r requirements.txt
CMD ["python", "app.py"]