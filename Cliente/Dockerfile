FROM bitnami/python:3.8.13

WORKDIR /code
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN python3 -m pip install grpcio
RUN python3 -m pip install grpcio-tools
RUN pip install flask
EXPOSE 5000
COPY . .
CMD ["flask", "run"]