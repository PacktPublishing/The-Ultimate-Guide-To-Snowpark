ARG BASE_IMAGE=continuumio/miniconda3:4.12.0   
FROM $BASE_IMAGE
RUN conda install python=3.8 && \
    conda install snowflake-snowpark-python
COPY main.py ./
ENTRYPOINT ["python3", "main.py"]
