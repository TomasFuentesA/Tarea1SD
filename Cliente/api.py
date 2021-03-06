from flask import Flask, render_template, request   

import grpc
import redis
import logging
import proto_message_pb2 as pb2_grpc
import proto_message_pb2_grpc as pb2
import time
import json

app = Flask(__name__)

r = redis.Redis(host="redis", port=6379, db=0)
r.config_set('maxmemory', 865200*2)
r.config_set('maxmemory-policy', 'allkeys-lru')
r.flushall()

class SearchClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'server_grpc'
        self.server_port = '50051'

        # instantiate a channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2.SearchStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2_grpc.Message(message=message)
        print(f'{message}')
        stub = self.stub.GetServerResponse(message)
        return stub


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods = ['GET'])
def search():
    client = SearchClient()
    search = request.args['search']
    cache = r.get(search)
    if cache == None:
        item = client.get_url(message=search)
        
        r.set(search, str(item))
        return render_template('index.html', datos = item, procedencia = "Datos sacados de PostgreSQL")
    else:
        print(cache)
        item = cache.decode("utf-8")
        print(item)
        dicc = dict()
        dicc['Resultado'] = item
        print(cache)
        return render_template('index.html', datos = item, procedencia = "Datos sacados de Redis")

if __name__ == '__main__':
    time.sleep(25)
    #result = client.get_url(message="Hello Server you there?")
    #print(result.product[0].name + "*******")
    #print(f'{result}')
