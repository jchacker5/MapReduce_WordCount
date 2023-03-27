class ReducerTask:
    def __init__(self, key):
        self.key = key
        self.count = 0

    def update_count(self, count):
        self.count += count
