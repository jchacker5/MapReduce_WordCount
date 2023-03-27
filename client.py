from master import Master
from config import input_file_path, machine_ips

def main():
    master = Master(machine_ips, input_file_path)
    master.start_job()

if __name__ == "__main__":
    main()
