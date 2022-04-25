from flask import Flask, render_template, request
import grpc
import proto_message_pb2
import proto_message_pb2_grpc



app = Flask(__name__)

def query_request(consulta):
    channel = grpc.insecure_channel('localhost:50051')
    grpc.channel_ready_future(channel).result(timeout=10)
    stub = proto_message_pb2_grpc.ItemServiceStub(channel)
    request = proto_message_pb2.GetItemsRequest(name=consulta)
    response = stub.GetItem(request)

    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods = ['GET'])
def search():
    search = request.args.get('search')
    #sv_response = query_request(search)

    return render_template('index.html', datos = search)