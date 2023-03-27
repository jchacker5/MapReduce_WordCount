class ReducerTask:
    def __init__(self, key):
        # Initialize the ReducerTask instance with a key (word) and a count of 0
        self.key = key
        self.count = 0

    def update_count(self, count):
        # Update the count of the ReducerTask instance by adding the given count
        self.count += count
