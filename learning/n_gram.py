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
#can try another data set
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
#We can access the mapping of words to integers as a dictionary attribute called word_index on the Tokenizer object.
#We need to know the size of the vocabulary for defining the embedding layer later. 
#We can determine the vocabulary by calculating the size of the mapping dictionary.
#Words are assigned values from 1 to the total number of words.
#The Embedding layer needs to allocate a vector representation for each word in this vocabulary 
#from index 1 to the largest index and because indexing of arrays is zero-offset, 
#the index of the word at the end of the vocabulary will be (tokenizer.word_index); 
#that means the array must be (tokenizer.word_index+1) in length.
#Therefore, when specifying the vocabulary size to the Embedding layer, 
#we specify it as 1 larger than the actual vocabulary.


tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)
# vocabulary size
vocab_size = len(tokenizer.word_index) + 1
 
# separate into input and output
sequences = array(sequences)
#X, y = sequences[:,:-1], sequences[:,-1]
X = sequences[:,-1]
y = sequences[:,-1]

y = to_categorical(y, num_classes=vocab_size)
seq_length = X.shape[1]
 
# define model
#Now we need to separate input sequence into input (X) and output (y) elements.
# We do this with array slicing.
#After separating, we need to one hot encode the output word. 
#This means converting it from an integer to a vector of 0 values, 
#one for each word in the vocabulary, with a 1 to indicate the specific word at the index of the words integer value.
#This is so that the model learns to predict the probability distribution for the next word 
#and the ground truth from which to learn from is 0 for all words except the actual word that comes next.
#Keras provides the to_categorical() that can be used to one hot encode the output words for each input-output sequence pair.
#we also need to specify to the Embedding layer how long input sequences are.
#We already know that there are 50 words because we designed the model, 

#We can now define and fit our language model on the training data.
#The learned embedding needs to know the size of the vocabulary and the length of input sequences as previously discussed. 
#It also has a parameter to specify how many dimensions will be used to represent each word. 
#That is, the size of the embedding vector space.
#Common values are 50, 100, and 300. We will use 50 here, but consider testing smaller or larger values.
#We will use a two LSTM hidden layers with 100 memory cells each. 
#More memory cells and a deeper network may achieve better results.
#A dense fully connected layer with 100 neurons connects to the LSTM hidden layers 
#to interpret the features extracted from the sequence. 
#The output layer predicts the next word as a single vector the size of the vocabulary with a probability for each word 
#in the vocabulary. 
#A softmax activation function is used to ensure the outputs have the characteristics of normalized probabilities.
#Next, the model is compiled specifying the categorical cross entropy loss needed to fit the model. 
#Technically, the model is learning a multi-class classification 
#and this is the suitable loss function for this type of problem. 
#The efficient Adam implementation to mini-batch gradient descent is used and accuracy is evaluated of the model.
#the model is fit on the data for 100 training epochs with a modest batch size of 128 to speed things up. 



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
