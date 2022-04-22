import grpc
from concurrent import futures
import proto_message_pb2
import proto_message_pb2_grpc

class buscar(proto_message_pb2_grpc.ItemServiceServicer):

    def __init__(self):
        print("Inicialización correcta")

    def GetServerResponse(self, request, context):
        print ("Hola mundo")


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto_message_pb2_grpc.add_ItemServiceServicer_to_server(buscar(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()