import grpc
from word_count_pb2 import *
from word_count_pb2_grpc import *

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
