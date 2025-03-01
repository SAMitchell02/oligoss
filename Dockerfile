FROM python:3.7.17

RUN pip install oligoss

ENV data_dir="/input/data"
ENV output_dir="/input/output"
ENV input_params="/input/input_parameters.json"

ENTRYPOINT python -m oligoss -i $input_params -r $data_dir -o $output_dir