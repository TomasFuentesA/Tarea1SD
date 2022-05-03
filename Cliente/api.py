from flask import Flask, render_template, request   

import grpc

import logging
import proto_message_pb2 as pb2_grpc
import proto_message_pb2_grpc as pb2



class SearchClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.SearchStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = SearchClient()
    result = client.get_url(message="Hello Server you there?")
    print(result.product[0].name + "*******")
    print(f'{result}')

'''
app = Flask(__name__)

class fetchItem(object):
    def __init__(self):
        self.channel = grpc.insecure_channel('server_grpc:50051')
        self.stub = proto_message_pb2_grpc.ItemServiceStub(self.channel)
    
    def get_item(self, name):
        request = proto_message_pb2.GetItemsRequest(name=name)
        response = self.stub.GetItem(request)
        return response

def custom_get_one_item(stub, name):
    nombre = stub.GetItem(name)
    print("Feater called with id %d returned: %s" %(name,nombre))
    return

def custom_get_item(stub, string):
    custom_get_one_item(stub, name=string)

def query_request(consulta):
    channel = grpc.insecure_channel('server_grpc:50051')
    grpc.channel_ready_future(channel).result(timeout=10)
    stub = proto_message_pb2_grpc.ItemServiceStub(channel)
    #request = proto_message_pb2.GetItemsRequest(name=consulta)
    #response = stub.GetItem(request)
    #if redos
    #else postgres then edit redis
    response = stub.GetItem(proto_message_pb2.GetItemsRequest(name=consulta))
    custom_get_item(stub, response)
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods = ['GET'])
def search():
    client = fetchItem()
    search = request.args.get('search')
    print(search)
    item = client.get_item(search)
    print(item)
    #sv_response = query_request(search)
    

    return render_template('index.html', datos = search)
'''    