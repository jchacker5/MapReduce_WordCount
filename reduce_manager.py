import grpc
from map_manager import MapManager
from word_count_pb2_grpc import add_MapManagerServicer_to_server


class ReduceManager(ReduceManagerServicer):
    def __init__(self):
        self.reducer_tasks = {}

    def get_or_create_reducer_task(self, key):
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
