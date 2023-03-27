from reducer_task import ReducerTask

class ReduceManager:
    def __init__(self):
        self.reducer_tasks = {}

    def get_or_create_reducer_task(self, key):
        if key not in self.reducer_tasks:
            self.reducer_tasks[key] = ReducerTask(key)
        return self.reducer_tasks[key]
