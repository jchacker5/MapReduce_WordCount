import grpc
from concurrent import futures
from word_count_pb2 import *
from word_count_pb2_grpc import *

# Define the ReducerTask class to keep track of word counts for a specific key (word)
class ReducerTask:
    def __init__(self, key):
        self.key = key
        self.count = 0

    # Method to update the count for a specific key (word)
    def update_count(self, count):
        self.count += count

# Define the ReduceManager class, which inherits from the auto-generated ReduceManagerServicer class
class ReduceManager(ReduceManagerServicer):
    def __init__(self):
        # Initialize an empty dictionary to store the ReducerTask instances
        self.reducer_tasks = {}

    # Implement the GetOrCreateReducerTask method, which takes a request object and a context object
    def GetOrCreateReducerTask(self, request, context):
        # Extract the key (word) from the request object
        key = request.key
        # Check if a ReducerTask instance for the given key already exists
        if key not in self.reducer_tasks:
            # If not, create a new ReducerTask instance for the key and store it in the reducer_tasks dictionary
            self.reducer_tasks[key] = ReducerTask(key)
        # Return the ReducerTask instance corresponding to the key
        return self.reducer_tasks[key]

# Define the serve function, which creates a gRPC server and starts it
def serve():
    # Create a server object with a thread pool executor with 10 worker threads
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Add the ReduceManagerServicer implementation to the server
    add_ReduceManagerServicer_to_server(ReduceManager(), server)
    # Add an insecure port for the server to listen on (in this case, port 50053)
    server.add_insecure_port('[::]:50053')
    # Start the server
    server.start()
    print('Reduce Manager node started on port 50053')
    # Wait for the server to be terminated
    server.wait_for_termination()

# If this file is executed directly (not imported), run the serve function to start the server
if __name__ == "__main__":
    serve()
