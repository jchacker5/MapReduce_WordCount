import grpc
from concurrent import futures
from word_count_pb2 import *
from word_count_pb2_grpc import *

class ReducerTask:
    def __init__(self, key):
        self.key = key
        self.count = 0

    def update_count(self, count):
        self.count += count

class ReduceManager(ReduceManagerServicer):
    def __init__(self):
        self.reducer_tasks = {}

    def GetOrCreateReducerTask(self, request, context):
        key = request.key
        if key not in self.reducer_tasks:
            self.reducer_tasks[key] = ReducerTask(key)
        return self.reducer_tasks[key]

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ReduceManagerServicer_to_server(ReduceManager(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print('Reduce Manager node started on port 50053')
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
