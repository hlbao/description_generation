import os
import logging

from unidecode import unidecode
import spacy

from constants import *


def clean(in_path, out_path, nlp):
	"""Clean sentences in in_path, then writes them in out_path."""
	logging.debug('IN')
	all_files = os.listdir(in_path)
	for file in all_files:
		# clean input files lines (lines is a set())
		lines = read_in(in_path, file, nlp)
		# write cleaned lines in output file
		write_out(lines, out_path, file)


def roman_numbers(line):
	logging.debug(line)
	m = R_CENT_ROMAN.search(line)
	while m:
		replacement = m.group(0)
		logging.debug('roman number found - {}'.format(replacement))
		line = line.replace(replacement, R_ROMAN.sub(NUM_TOKEN, replacement), 1)
		m = R_CENT_ROMAN.search(line)
	return line


def write_out(lines, path, file):
	"""Write lines in file located at path."""
	logging.debug('IN')
	with open(path+file, 'w') as output_file:
		logging.info('Writing {} lines in {}{}'.format(len(lines), path, file))
		for line in lines: # just in case
			output_file.write(line+'\n')

def formulas(line):
	logging.debug(line)
	return R_FORMULA.sub(FORMULA_TOKEN, line)

def decimal_numbers(line):
	"""Finds and replaces decimal numbers for unique token."""
	logging.debug(line)
	return R_NUM.sub(NUM_TOKEN, line)

def surrounded(line):
	"""Finds and removes <tags>."""
	logging.debug(line)
	line = R_TAG.sub('', line)
	line = R_PARENTHESIS.sub('', line)
	return line


def entities(nlp, line):
	logging.debug(line)
	for ent in nlp(line).ents:
		logging.debug('Found entity "{}", {}'.format(ent.text, ent.label_))
		line = line.replace(ent.text, ent.label_)
	return line


def to_lower(line):
	"""Gets everything lower."""
	logging.debug(line)
	return ' '.join([w if w in TOKENS else w.lower() for w in line.split()])

def separate_tokens(line):
	logging.debug(line)
	for TOKEN in TOKENS:
		line = line.replace(TOKEN, ' {} '.format(TOKEN))
	return line

def read_in(path, file, nlp):
	"""Reads lines in files located in path and sends them to be cleaned."""
	logging.debug('IN')
	lines = set()
	with open(path+file, 'r') as inputfile:
		logging.info('Cleaning {}{}'.format(path, file))
		raw_line = inputfile.readline()
		while raw_line:
			for i, sent in enumerate(nlp(raw_line).sents):
				line = clean_line(nlp, sent.text.replace('\n', ''))
				if line != None:
					lines.add(line)
			raw_line = inputfile.readline()
	return lines

def keep(line):
	logging.debug(line)
	word_list = line.split()
	n_words = len(word_list)
	# control words number
	if n_words < 8 or n_words > 20:
		return False
	n_tokens = len(list(filter(lambda x: x in TOKENS, word_list)))
	# excesive number of tokens
	return n_tokens/(n_words-1)<=TOKEN_THROW_RATIO

def alphanumeric(line):
	"""Replaces special characters with white spaces."""
	logging.debug(line)
	return ''.join(e if e.isalnum() else ' ' for e in line)



def clean_line(nlp, line):
	logging.debug('Cleaning \"{}\"'.format(line))
	line = surrounded(line)
	line = entities(nlp, line)
	line = formulas(line)
	line = decimal_numbers(line)
	line = roman_numbers(line)
	line = separate_tokens(line)
	line = unidecode(line)
	line = alphanumeric(line)
	line = to_lower(line)
	return line if keep(line) else None


if __name__ == '__main__':
	logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
	#logging.info('Loading model - {}'.format(ES_MODEL))
	#nlp = spacy.load(ES_MODEL)
  #logging.info('Loading model - {}'.format(EN_MODEL))
	#nlp = spacy.load(EN_MODEL)
	clean(MINED_FOLDER, CLEANED_FOLDER, nlp)


