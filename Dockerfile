FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python", "app/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]