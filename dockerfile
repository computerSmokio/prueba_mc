from python:3.9.18-alpine3.18 as dev
# Install the dependencies
copy requirements/dev.txt /tmp/requirements.txt
run pip install -r /tmp/requirements.txt
# Copy the app code
workdir /app
copy src /app/src
run mkdir /app/logs /app/data
copy .env /app
ENTRYPOINT ["python", "src/main.py"]


from python:3.9.18-alpine3.18 as prod
# Install the dependencies
copy requirements/minimal.txt /tmp/requirements.txt
run pip install -r /tmp/requirements.txt
# Copy the app code
workdir /app
copy src/api /app/src/api
copy src/main.py /app/src
# Create an unprivileged user to run the app with no shell
run adduser -s /bin/false -D -H -u 1000 app_user
run chown app_user /app
run chmod -R 710 /app
run mkdir /var/log/app /app/data
run chown -R app_user /var/log/app /app
run chmod -R 710 /var/log/app /app/data
ENV LOG_DIR=/var/log/app

USER app_user
ENTRYPOINT ["python", "src/main.py"]
