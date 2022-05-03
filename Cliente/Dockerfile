FROM bitnami/python:3.8.13

WORKDIR /code
COPY proto_message.proto ./

RUN python3 -m pip install grpcio
RUN python3 -m pip install grpcio-tools
RUN python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./proto_message.proto

RUN pip install flask
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
COPY . .
CMD ["python3", "api.py"]