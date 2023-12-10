FROM python:3.10.8

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the app folder to the container at /app
COPY ./app /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80


ENTRYPOINT ["python", "./manage.py"]
CMD ["runserver", "0.0.0.0:8000"]