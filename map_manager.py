import grpc
from concurrent import futures
from word_count_pb2 import *
from word_count_pb2_grpc import *

class MapperTask:
    def __init__(self, input_line):
        self.input_line = input_line

    # Implement other methods for MapperTask

class MapManager(MapManagerServicer):
    def __init__(self):
        self.mapper_tasks = []

    def create_mapper_task(self, input_line):
        mapper_task = MapperTask(input_line)
        self.mapper_tasks.append(mapper_task)
        return mapper_task

    def CreateMapTask(self, request, context):
        # Implement the gRPC method for creating a mapper task
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MapManagerServicer_to_server(MapManager(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print('Map Manager node started on port 50052')
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
