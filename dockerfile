from python:3.9.18-alpine3.18 as dev
# Install the dependencies
copy requirements/dev.txt /tmp/requirements.txt
run pip install -r /tmp/requirements.txt
# Copy the app code
workdir /app
copy src /app/src
run mkdir /app/logs /app/data
copy .env /app
ENV LOG_DIR=/app/logs
ENV JSON_DIR=/app/data
ENTRYPOINT ["python", "src/main.py"]


from python:3.9.18-alpine3.18 as build_maker
# Install the dependencies
run pip install cython
run apk add gcc build-base
# Copy the app code
workdir /app
copy src/api /app/src/api
copy src/static /app/src/static
copy src/main.py /app/src
copy src/setup.py /app/src
run python src/setup.py build_ext --inplace

from python:3.9.18-alpine3.18 as prod
copy requirements/minimal.txt /tmp/requirements.txt
run pip install -r /tmp/requirements.txt
# Copy compiled api
workdir /app
copy --from=build_maker /app/build /app/src
run mkdir /var/log/app /app/data

# Create an unprivileged user to run the app with no shell
run adduser -s /bin/false -D -H -u 1001 app_user
run chmod -R 710 /app /var/log/app
run chown -R app_user:app_user /app /var/log/app
ENV LOG_DIR=/var/log/app
ENV JSON_DIR=/app/data

USER root
CMD ["python", "src/main.py"]
