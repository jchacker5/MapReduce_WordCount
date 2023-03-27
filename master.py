from map_manager import MapManager
from reduce_manager import ReduceManager
from config import input_file_path, machine_ips

class Master:
    def __init__(self, machine_ips, input_file_path):
        self.machine_ips = machine_ips
        self.input_file_path = input_file_path
        self.map_manager = MapManager()
        self.reduce_manager = ReduceManager()

    def start_job(self):
        with open(self.input_file_path, 'r') as input_file:
            for line in input_file:
                # Create a mapper task for each line in the input file
                mapper_task = self.map_manager.create_mapper_task(line)

                # Process the input line and get the word count dictionary
                word_count_dict = mapper_task.process_line()

                # Get or create reducer tasks for each word and update the count
                for word, count in word_count_dict.items():
                    reducer_task = self.reduce_manager.get_or_create_reducer_task(word)
                    reducer_task.update_count(count)

        # Write the final word count to an output file
        with open('output.txt', 'w') as output_file:
            for word, reducer_task in self.reduce_manager.reducer_tasks.items():
                output_file.write(f'{word}: {reducer_task.count}\n')

        print("Job completed. Output written to 'output.txt'.")
