import grpc
from concurrent import futures
import proto_message_pb2
import proto_message_pb2_grpc
from psycopg2 import connect

class buscar(proto_message_pb2_grpc.ItemServiceServicer):

    def __init__(self):
        print("Inicialización correcta")

    def GetServerResponse(self, request, context):
        print ("Hola mundo")

def db_con():
    conn = connect(host="postgres" ,dbname="Tarea1", user="postgres", password="postgres", port= 5432)
    return conn

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto_message_pb2_grpc.add_ItemServiceServicer_to_server(buscar(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    conn = db_con()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Items;")
    for i, record in enumerate(cursor):
        print ("\n", type(record))
        print ( record )

    # close the cursor object to avoid memory leaks
    cursor.close()

    server.wait_for_termination()


if __name__ == '__main__':
    serve() 