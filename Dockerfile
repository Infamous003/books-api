FROM python:latest

COPY app.py /app/
COPY database.py /app/
COPY models.py /app/
COPY requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]