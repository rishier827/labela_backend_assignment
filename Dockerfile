FROM python:3.10
LABEL author='Label A'

WORKDIR /app

# Environment
RUN apt-get update
RUN apt-get install -y bash vim nano postgresql-client
RUN pip install --upgrade pip

# Major pinned python dependencies
RUN pip install --no-cache-dir flake8==3.8.4 uWSGI

# Regular Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy our codebase into the container
COPY . .

RUN ./manage.py collectstatic --noinput

# Ops Parameters
ENV WORKERS=2
ENV PORT=8000
ENV PYTHONUNBUFFERED=1
ENV DB_NAME=postgres
ENV DB_USER=postgres
ENV DB_PASSWORD=postgres
ENV DB_HOST=db
ENV DB_PORT=5432

# Create superuser params
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=123@QWEasd
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com

EXPOSE ${PORT}

CMD python manage.py migrate && \
    uwsgi --http :${PORT} --processes ${WORKERS} --static-map /static=/static --module autocompany.wsgi:application && \
    python manage.py runserver
