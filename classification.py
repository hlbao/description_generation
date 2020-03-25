#we will use an Embedding Layer to learn the distributed representation of words 
# which aims to achieve that different words with similar meanings will have a similar representation, 
#and a Long Short-Term Memory (LSTM) recurrent neural network to learn to predict words based on their context.


from numpy import array
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding
 
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
 
# load
in_filename = 'cleaned.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')
 

# The word embedding layer expects input sequences to be comprised of integers.
#We can map each word in our vocabulary to a unique integer and encode our input sequences. 
#Later, when we make predictions, 
#we can convert the prediction to numbers and look up their associated words in the same mapping.
#To do this encoding, we will use the Tokenizer class in the Keras API.
#First, the Tokenizer must be trained on the entire training dataset, 
#which means it finds all of the unique words in the data and assigns each a unique integer.
#We can then use the fit Tokenizer to encode all of the training sequences, 
#converting each sequence from a list of words to a list of integers.

tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)
# vocabulary size
vocab_size = len(tokenizer.word_index) + 1
 
# separate into input and output
sequences = array(sequences)
X, y = sequences[:,:-1], sequences[:,-1]
y = to_categorical(y, num_classes=vocab_size)
seq_length = X.shape[1]
 
# define model
model = Sequential()
model.add(Embedding(vocab_size, 50, input_length=seq_length))
model.add(LSTM(100, return_sequences=True))
model.add(LSTM(100))
model.add(Dense(100, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())
# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, batch_size=128, epochs=100)
 
# save the model to file
model.save('model.h5')
# save the tokenizer
dump(tokenizer, open('tokenizer.pkl', 'wb'))
