FROM python:3.9-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=settings.local

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && bash scripts/populate_db.sh 100 && python manage.py runserver 0.0.0.0:8000"]




