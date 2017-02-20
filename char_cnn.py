import tensorflow as tf
import numpy as np

class CharacterRNN(object):
    def __init__(self, input_vocab_size, input_size, output_size, filter_sizes):
        self.input_vocabulary_size = input_vocab_size
        self.input_size = input_size
        self.output_size = output_size
        self.filter_sizes = filter_sizes

    def BuildModel(self, input, output, dropout_prob = None):
        for layer_i, 

