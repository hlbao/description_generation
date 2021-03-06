import string
#from clean import clean_line, alphanumeric, keep, separate_tokens, to_lower, entities, surrounded, decimal_numbers

#from clean import formulas, roman_numbers, write_out, roman_numbers, clean, read_in
 
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
 
# turn a doc into tokens
def get_doc(doc):
	tokens = doc.split()
	return tokens
 
# save tokens to file, one dialog per line
def save_doc(lines, filename):
	data = '\n'.join(lines)
	file = open(filename, 'w')
	file.write(data)
	file.close()
 
# load document
in_filename = 'cleaned.txt'
doc = load_doc(in_filename)
print(doc[:200])
 
# clean document
tokens = get_doc(doc)
print(tokens[:200])
print('Total Tokens: %d' % len(tokens))
print('Unique Tokens: %d' % len(set(tokens)))
 
# organize into sequences of tokens
length = 50 + 1
sequences = list()
for i in range(length, len(tokens)):
	# select sequence of tokens
	seq = tokens[i-length:i]
	# convert into a line
	line = ' '.join(seq)
	# store
	sequences.append(line)
print('Total Sequences: %d' % len(sequences))
 
# save sequences to file
out_filename = 'cleaned.txt'
save_doc(sequences, out_filename)
