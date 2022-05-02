import grpc
from concurrent import futures
import proto_message_pb2
import proto_message_pb2_grpc
from psycopg2 import connect
from time import sleep
import logging
import server_resources


def get_item(name):
   print(name)
class buscar(proto_message_pb2_grpc.ItemServiceServicer):

    def __init__(self):
        logging.info("Inicialización correcta")

    def GetServerResponse(self, request, context):
        print ("Hola mundo")

    def GetItem(self, request, context):
        return proto_message_pb2.Item(**data.get(request.name, {}))


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto_message_pb2_grpc.add_ItemServiceServicer_to_server(buscar(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    sleep(20)
    conn = server_resources.init_db()
    '''

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Items;")
    for i, record in enumerate(cursor):
        print ("\n", type(record))
        print ( record )

    # close the cursor object to avoid memory leaks
    cursor.close()

    
    '''
    

    server.wait_for_termination()

data = {
    "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops": {"price": 109.95, "category":'mens clothing',"count": 120}
}

if __name__ == '__main__':
    serve() 