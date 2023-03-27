from mapper_task import MapperTask

class MapManager:
    def __init__(self):
        self.mapper_tasks = []

    def create_mapper_task(self, input_line):
        mapper_task = MapperTask(input_line)
        self.mapper_tasks.append(mapper_task)
        return mapper_task
