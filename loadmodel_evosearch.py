import sys
import random
import multiprocessing
import numpy
from deap import creator, base, tools, algorithms
from random import randint
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
 
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text


# load cleaned text sequences
in_filename = 'cleaned.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')
seq_length = len(lines[0].split()) - 1
 
# load the model
model = load_model('model.h5')
 
# load the tokenizer
tokenizer = load(open('tokenizer.pkl', 'rb'))

