FROM python:3.9-slim

# Install gettext for translation tools
RUN apt-get update && apt-get install -y gettext

WORKDIR /app

# Copy requirements and install them
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Ensure the settings module is available
ENV DJANGO_SETTINGS_MODULE=djangomllm.settings

# Run compilemessages after setting up the context
RUN python manage.py compilemessages -l fr

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djangomllm.wsgi:application"]
