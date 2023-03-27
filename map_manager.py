import grpc
from concurrent import futures
from word_count_pb2 import *
from word_count_pb2_grpc import *

class MapperTask:
    def __init__(self, input_line):
        """
        Initializes the MapperTask with the given input line.

        Args:
        - input_line: A string representing the input line for the mapper task.
        """
        self.input_line = input_line

    # Other methods for MapperTask implementation go here

class MapManager(MapManagerServicer):
    def __init__(self):
        """
        Initializes the MapManager with an empty list of mapper tasks.
        """
        self.mapper_tasks = []

    def create_mapper_task(self, input_line):
        """
        Creates a new mapper task for the given input line.

        Args:
        - input_line: A string representing the input line to be processed by the mapper task.

        Returns:
        A MapperTask instance representing the newly created mapper task.
        """
        mapper_task = MapperTask(input_line)
        self.mapper_tasks.append(mapper_task)
        return mapper_task

    def CreateMapTask(self, request, context):
        """
        Implements the gRPC method for creating a mapper task.

        Args:
        - request: A CreateMapTaskRequest instance representing the request.
        - context: A grpc.ServicerContext instance representing the context.

        Returns:
        A CreateMapTaskResponse instance representing the response.
        """
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
