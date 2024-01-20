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

EXPOSE ${PORT}

# Make the wait-for-postgres.sh script executable
COPY ./wait-for-postgres.sh /wait-for-postgres.sh
RUN chmod +x /wait-for-postgres.sh

CMD /wait-for-postgres.sh db set -xe; \
    python3 manage.py collectstatic --noinput --clear; \
    python3 manage.py migrate --noinput; \
    python3 manage.py loaddata fixtures/*.json; \
    python manage.py createadmin --username 'superadmin' --password '1234' --email 'superadmin@example.com'; \
    python manage.py runserver 0.0.0.0:8000
