ARG BASE_IMAGE=python:3.10-slim-buster
FROM $BASE_IMAGE
COPY filter_service.py ./
COPY templates/ ./templates/
RUN pip install --upgrade pip && \
    pip install flask && \
    pip install snowflake-snowpark-python[pandas]
CMD ["python3", "echo_service.py"]
