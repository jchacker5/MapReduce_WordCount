from map_manager import MapManager
from reduce_manager import ReduceManager
from config import input_file_path, machine_ips
import utils

class Master:
    def __init__(self, machine_ips, input_file_path):
        self.machine_ips = machine_ips
        self.input_file_path = input_file_path
        self.map_manager = MapManager()
        self.reduce_manager = ReduceManager()

    def start_job(self):
        # Implement the master node logic here
        pass

def main():
    master = Master(machine_ips, input_file_path)
    master.start_job()

if __name__ == "__main__":
    main()
