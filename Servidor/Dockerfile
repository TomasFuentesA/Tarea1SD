FROM bitnami/python:3.8.13


COPY proto_message.proto ./
COPY server_grpc.py ./
COPY server_resources.py ./

RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools
RUN python -m pip install psycopg2-binary

RUN python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./proto_message.proto

CMD [ "python3", "server_grpc.py" ]