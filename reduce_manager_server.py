import grpc
from concurrent import futures
from reduce_manager import ReduceManager
from word_count_pb2_grpc import add_ReduceManagerServicer_to_server

# Define the serve function, which starts the gRPC server for the Reduce Manager node
def serve():
    # Create a gRPC server with a ThreadPoolExecutor for handling incoming requests
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Add the ReduceManager service to the server
    add_ReduceManagerServicer_to_server(ReduceManager(), server)
    # Specify the address and port on which the server will listen for incoming connections
    server.add_insecure_port('[::]:50053')
    # Start the server
    server.start()
    # Print a message indicating that the Reduce Manager node has started
    print('Reduce Manager node started on port 50053')
    # Wait for the server to be terminated
    server.wait_for_termination()

# Run the serve function when the script is executed
if __name__ == "__main__":
    serve()
