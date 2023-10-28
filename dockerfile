from python:3.9.18-alpine3.18 as dev
# Install the dependencies
copy requirements/dev.txt /tmp/requirements.txt
run pip install -r /tmp/requirements.txt
# Copy the app code
workdir /app
copy src /app
copy .env /app
ENTRYPOINT ["python", "src/main.py"]


from python:3.9.18-alpine3.18 as prod
# Install the dependencies
copy requirements/minimal.txt /tmp/requirements.txt
run pip install -r /tmp/requirements.txt
# Copy the app code
workdir /app
copy src/api /app/src
copy src/main.py /app/src
# Create an unprivileged user to run the app
USER app_user
run CHOWN app_user:app_user /app
run chmod -R 710 /app
run mkdir /var/log/app
run chown app_user:app_user /var/log/app
run chmod -R 710 /var/log/app
ENV LOG_DIR=/var/log/app

ENTRYPOINT ["python", "src/main.py"]
