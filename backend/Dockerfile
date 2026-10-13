from python:3.14-slim

workdir /app

ENV PYTHONDONTWRITEBYCODE=1
ENV PYTHONUNBUFFERED=1

copy requirements.txt .
run pip install --no-cache-dir -r requirements.txt

copy . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]