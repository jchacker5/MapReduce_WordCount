import grpc
from word_count_pb2 import *
from word_count_pb2_grpc import *

class MapperTask:
    def __init__(self, input_line):
        self.input_line = input_line

    def process_line(self):
        # Split the input line into words
        words = self.input_line.split()

        # Create an empty dictionary to store the word count
        word_count_dict = {}

        # Count the occurrences of each word in the input line
        for word in words:
            if word not in word_count_dict:
                word_count_dict[word] = 1
            else:
                word_count_dict[word] += 1

        return word_count_dict
