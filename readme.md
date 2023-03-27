MapReduce-style Distributed Word Count Application
This is an implementation of a MapReduce-style distributed word count application using gRPC in Python.

Requirements
Python 3.6 or later
gRPC (installation instructions: https://grpc.io/docs/languages/python/quickstart/)
Installation
Clone this repository to your local machine.

Install the required dependencies by running the following command:


pip install -r requirements.txt
Usage
Start the gRPC servers for the master, map manager, and reduce manager nodes by running the serve() method in master.py, map_manager.py, and reduce_manager.py files respectively. You can do this by running each of these files in separate terminals using the python command:

python master.py
python map_manager.py
python reduce_manager.py
Once the servers are running, you can run the main() function in client.py using the python command. This will start the MapReduce job and write the output to a file named output.txt.


python client.py
After the job is completed, you can open the output.txt file to see the word count for each word in the input file.

Make sure that the input file is located in the directory specified in the input_file_path variable in the config.py file, and that the IP addresses of the machines running the map and reduce managers are listed in the machine_ips variable in the same file.

Credits
This implementation was created by Josph Defendre. Feel free to use it, modify it, or distribute it under the terms of the MIT License.