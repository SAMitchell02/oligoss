FROM python:3.7.17

RUN pip install oligoss

ENTRYPOINT python -m oligoss -i /input_parameters.json -r /data -o /output